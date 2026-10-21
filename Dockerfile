# ==============================================================================
# Dockerfile for Cold Storage Slot Booking System (CSBS)
# Student: Mayuresh Sawant (23102A0029)
# Subject: DevOps Lab | Evaluator: Dr. Snehal Andhare
# ==============================================================================

# ------------------------------------------------------------------------------
# STAGE 1: Build & Package (Maven Builder)
# ------------------------------------------------------------------------------
FROM maven:3.9.9-eclipse-temurin-21-alpine AS builder

WORKDIR /build

# Cache dependencies layer
COPY cold-storage-app/pom.xml ./pom.xml
RUN mvn dependency:go-offline -B

# Copy application source code and compile
COPY cold-storage-app/src ./src
RUN mvn clean package -DskipTests

# ------------------------------------------------------------------------------
# STAGE 2: Minimal Production Runtime (Alpine JRE)
# ------------------------------------------------------------------------------
FROM eclipse-temurin:21-jre-alpine

LABEL maintainer="Mayuresh Sawant <23102A0029@student.engg.edu>"
LABEL project="Cold Storage Slot Booking System"
LABEL version="1.0.0"

# Security hardening: Create non-root system group and user
RUN addgroup -S coldstorage && adduser -S coldstorage -G coldstorage

WORKDIR /app

# Copy compiled standalone executable JAR from builder stage
COPY --from=builder /build/target/coldstorage-app.jar /app/coldstorage-app.jar

# Enforce secure file ownership
RUN chown -R coldstorage:coldstorage /app

# Switch to unprivileged execution user
USER coldstorage

# Expose HTTP port
EXPOSE 8080

# Health check probe via Spring Boot Actuator
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:8080/actuator/health || exit 1

# Launch JVM with optimized container memory flags
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-XX:+UseG1GC", "-XX:MaxRAMPercentage=75.0", "-jar", "coldstorage-app.jar"]
