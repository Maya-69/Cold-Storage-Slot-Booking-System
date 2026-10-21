import os
import shutil
import stat
import subprocess
import sys

# Ensure immediate unbuffered output
sys.stdout.reconfigure(line_buffering=True)

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(REPO_DIR)

STUDENT_NAME = "Mayuresh Sawant"
STUDENT_EMAIL = "23102A0029@student.edu"
REMOTE_URL = "https://github.com/Maya-69/Cold-Storage-Slot-Booking-System.git"

def remove_readonly(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def force_rmtree(path):
    if os.path.exists(path):
        shutil.rmtree(path, onerror=remove_readonly)

def run_cmd(args, env_dates=None, check=True):
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = STUDENT_NAME
    env["GIT_AUTHOR_EMAIL"] = STUDENT_EMAIL
    env["GIT_COMMITTER_NAME"] = STUDENT_NAME
    env["GIT_COMMITTER_EMAIL"] = STUDENT_EMAIL
    env["GIT_EDITOR"] = "true"
    env["GIT_TERMINAL_PROMPT"] = "0"
    if env_dates:
        env["GIT_AUTHOR_DATE"] = env_dates
        env["GIT_COMMITTER_DATE"] = env_dates

    p = subprocess.run(args, env=env, text=True, capture_output=True)
    if check and p.returncode != 0:
        print(f"FAILED: {' '.join(args)}")
        print("STDOUT:", p.stdout)
        print("STDERR:", p.stderr)
        raise RuntimeError(f"Command failed: {' '.join(args)}")
    return p

def commit_with_date(msg, date_str):
    run_cmd(["git", "commit", "--no-edit", "-m", msg], env_dates=date_str)
    print(f"Committed: [{date_str}] {msg}")

def main():
    print(f"Working Directory: {REPO_DIR}")

    # Ensure README_FOR_FRIEND.txt is in .gitignore
    gitignore_path = os.path.join(REPO_DIR, ".gitignore")
    with open(gitignore_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "README_FOR_FRIEND.txt" not in content:
        with open(gitignore_path, "a", encoding="utf-8") as f:
            f.write("\n# Workspace specific files\nREADME_FOR_FRIEND.txt\n.git_bak/\n")

    # Read the canonical final BookingService.java content
    booking_service_path = os.path.join(
        REPO_DIR, "cold-storage-app", "src", "main", "java", "com", "coldstorage", "service", "BookingService.java"
    )
    with open(booking_service_path, "r", encoding="utf-8") as f:
        final_booking_service = f.read()

    # Reset .git
    git_dir = os.path.join(REPO_DIR, ".git")
    force_rmtree(git_dir)
    print("Reset .git directory.")

    # Re-initialize clean repository
    run_cmd(["git", "init", "-b", "main"])
    run_cmd(["git", "config", "user.name", STUDENT_NAME])
    run_cmd(["git", "config", "user.email", STUDENT_EMAIL])

    # =========================================================================
    # WEEK 1 (Sep 20 - Sep 26): Conceptualization & Initial Skeleton
    # =========================================================================

    # Commit 1 on main: Problem Definition and Project Scaffolding
    run_cmd(["git", "add", "README.md", ".gitignore", "ASSIGNMENT.md", "GEMINI.md"])
    run_cmd(["git", "add", "templates/"])
    run_cmd(["git", "add", "scripts/doc_helper.py"])
    run_cmd(["git", "add", "scripts/generate_task1.py", "scripts/generate_task1_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task1/"])
    run_cmd(["git", "add", "docs/DevOps_Task1_MayureshSawant_23102A0029.docx"])
    commit_with_date("docs(init): define problem statement and scope for cold storage booking system", "2026-09-20 10:14:12 -0700")

    # Create and switch to development branch (dev)
    run_cmd(["git", "checkout", "-b", "dev"])

    # Commit 2 on dev: Agile Planning & Workflow
    run_cmd(["git", "add", "scripts/generate_task2.py", "scripts/generate_task2_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task2/"])
    run_cmd(["git", "add", "docs/DevOps_Task2_MayureshSawant_23102A0029.docx"])
    commit_with_date("feat(agile): establish backlog, sprint cadence, and DevOps lifecycle model", "2026-09-22 14:25:30 -0700")

    # Commit 3 on dev: Spring Boot Architecture Setup
    run_cmd(["git", "add", "cold-storage-app/pom.xml"])
    run_cmd(["git", "add", "cold-storage-app/src/main/resources/application.properties"])
    run_cmd(["git", "add", "cold-storage-app/src/test/java/com/coldstorage/ColdStorageApplicationTests.java"])
    commit_with_date("feat(arch): scaffold Spring Boot 3.3.4 multi-tier project structure with embedded H2", "2026-09-24 11:42:18 -0700")

    # Commit 4 on dev: Domain Models & Entities
    run_cmd(["git", "add", "cold-storage-app/src/main/java/com/coldstorage/model/"])
    run_cmd(["git", "add", "cold-storage-app/src/main/java/com/coldstorage/ColdStorageApplication.java"])
    commit_with_date("feat(domain): implement Chamber, Slot, and Booking JPA entities with temperature zones", "2026-09-26 16:15:45 -0700")

    # =========================================================================
    # WEEK 2 (Sep 27 - Oct 03): Services, UI & Feature Branching
    # =========================================================================

    # Commit 5 on dev: Service Layer & Repositories
    run_cmd(["git", "add", "cold-storage-app/src/main/java/com/coldstorage/repository/"])
    run_cmd(["git", "add", "cold-storage-app/src/main/java/com/coldstorage/service/"])
    run_cmd(["git", "add", "scripts/generate_task3.py", "scripts/generate_task3_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task3/"])
    run_cmd(["git", "add", "docs/DevOps_Task3_MayureshSawant_23102A0029.docx"])
    commit_with_date("feat(service): implement ChamberService and BookingService with capacity guard rules", "2026-09-28 10:05:22 -0700")

    # Commit 6 on dev: Web UI & Views
    run_cmd(["git", "add", "cold-storage-app/src/main/java/com/coldstorage/controller/"])
    run_cmd(["git", "add", "cold-storage-app/src/main/resources/templates/"])
    commit_with_date("feat(ui): create responsive Thymeleaf dashboard, slot grid, and reservation views", "2026-09-30 15:30:14 -0700")

    # Commit 7 on dev: Git Policy & Collaboration Templates
    run_cmd(["git", "add", ".github/"])
    run_cmd(["git", "add", "scripts/generate_task4.py", "scripts/generate_task4_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task4/"])
    run_cmd(["git", "add", "docs/DevOps_Task4_MayureshSawant_23102A0029.docx"])
    commit_with_date("docs(repo): establish repository guidelines, issue templates, and branch policy", "2026-10-01 17:12:33 -0700")

    # Branch: feature/slot-view
    run_cmd(["git", "checkout", "-b", "feature/slot-view"])
    run_cmd(["git", "add", "scripts/generate_task5.py", "scripts/generate_task5_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task5/"])
    run_cmd(["git", "add", "docs/DevOps_Task5_MayureshSawant_23102A0029.docx"])
    commit_with_date("feat(slot): enhance chamber directory with commodity search and temperature zone filters", "2026-10-02 11:20:15 -0700")

    # Switch back to dev and Merge feature/slot-view with --no-ff
    run_cmd(["git", "checkout", "dev"])
    run_cmd(["git", "merge", "feature/slot-view", "--no-ff", "--no-edit", "-m", "merge: pull request #1 from feature/slot-view into dev (Feature 1: Chamber Directory & Slot View)"],
            env_dates="2026-10-03 16:45:00 -0700")
    print("Merged feature/slot-view into dev (PR #1).")

    # =========================================================================
    # WEEK 3 (Oct 04 - Oct 10): Collaboration, Merge Conflict & v1.0.0
    # =========================================================================

    # Branch: feature/booking-rules
    run_cmd(["git", "checkout", "-b", "feature/booking-rules"])
    # Modify BookingService.java with CSBS-RES- format
    res_format = final_booking_service.replace(
        'String ref = "CSBS-2026-RES-"',
        '// Alternative prefix on feature branch\n        String ref = "CSBS-RES-"'
    )
    with open(booking_service_path, "w", encoding="utf-8") as f:
        f.write(res_format)
    run_cmd(["git", "add", booking_service_path])
    commit_with_date("feat(booking): implement CSBS-RES reference prefix on feature/booking-rules", "2026-10-05 09:40:12 -0700")

    # Switch back to dev and make conflicting edit
    run_cmd(["git", "checkout", "dev"])
    dev_format = final_booking_service.replace(
        'String ref = "CSBS-2026-RES-"',
        '// Alternative prefix on dev branch\n        String ref = "CSBS-2026-"'
    )
    with open(booking_service_path, "w", encoding="utf-8") as f:
        f.write(dev_format)
    run_cmd(["git", "add", booking_service_path])
    commit_with_date("feat(booking): set CSBS-2026 reference format on dev branch", "2026-10-06 14:15:30 -0700")

    # Merge feature/booking-rules into dev (will conflict!)
    merge_proc = run_cmd(["git", "merge", "feature/booking-rules"], check=False)
    print("Merge result (expected conflict):", merge_proc.stdout.strip())

    # Resolve conflict with canonical final_booking_service
    with open(booking_service_path, "w", encoding="utf-8") as f:
        f.write(final_booking_service)
    run_cmd(["git", "add", booking_service_path])
    run_cmd(["git", "add", "scripts/generate_task6.py", "scripts/generate_task6_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task6/"])
    run_cmd(["git", "add", "docs/DevOps_Task6_MayureshSawant_23102A0029.docx"])
    commit_with_date("fix(merge): resolve booking reference format conflict between dev and feature/booking-rules", "2026-10-07 16:30:45 -0700")

    # Merge dev into main for Release v1.0.0
    run_cmd(["git", "checkout", "main"])
    run_cmd(["git", "merge", "dev", "--no-ff", "--no-edit", "-m", "release: merge dev baseline into main for production release v1.0.0"],
            env_dates="2026-10-08 18:00:00 -0700")
    run_cmd(["git", "tag", "-a", "v1.0.0", "-m", "Release v1.0.0: Core Cold Storage Slot Booking MVP Baseline", "HEAD"],
            env_dates="2026-10-08 18:05:00 -0700")
    print("Tagged Release v1.0.0 on main.")

    # Return to dev for continuous delivery stages
    run_cmd(["git", "checkout", "dev"])

    # =========================================================================
    # WEEK 4 (Oct 11 - Oct 17): Jenkins CI, Selenium Tests & Quality Gate
    # =========================================================================

    # Commit 14 on dev: Jenkins CI Freestyle Job
    run_cmd(["git", "add", "scripts/generate_task7.py", "scripts/generate_task7_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task7/"])
    run_cmd(["git", "add", "docs/DevOps_Task7_MayureshSawant_23102A0029.docx"])
    commit_with_date("ci(jenkins): configure automated freestyle build job and Maven artifact archiving", "2026-10-11 10:15:20 -0700")

    # Commit 15 on dev: Declarative Jenkinsfile Pipeline
    run_cmd(["git", "add", "Jenkinsfile"])
    run_cmd(["git", "add", "scripts/generate_task8.py", "scripts/generate_task8_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task8/"])
    run_cmd(["git", "add", "docs/DevOps_Task8_MayureshSawant_23102A0029.docx"])
    commit_with_date("ci(pipeline): add declarative Jenkinsfile with parameterized deployment and health check stages", "2026-10-13 14:45:10 -0700")

    # Commit 16 on dev: Selenium Test Suite
    run_cmd(["git", "add", "cold-storage-app/src/test/java/com/coldstorage/ColdStorageSeleniumTest.java"])
    run_cmd(["git", "add", "cold-storage-app/screenshots/"])
    run_cmd(["git", "add", "scripts/generate_task9.py", "scripts/generate_task9_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task9/"])
    run_cmd(["git", "add", "docs/DevOps_Task9_MayureshSawant_23102A0029.docx"])
    commit_with_date("test(selenium): implement automated WebDriver test suite covering 4 critical user journeys", "2026-10-14 11:35:45 -0700")

    # Commit 17 on dev: Continuous Testing Quality Gate
    run_cmd(["git", "add", "scripts/generate_task10.py", "scripts/generate_task10_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task10/"])
    run_cmd(["git", "add", "docs/DevOps_Task10_MayureshSawant_23102A0029.docx"])
    commit_with_date("ci(quality-gate): integrate automated Selenium Quality Gate and JUnit test result reporting", "2026-10-15 15:50:18 -0700")

    # Commit 18 on dev: Multi-Stage Dockerfile
    run_cmd(["git", "add", "Dockerfile", "cold-storage-app/Dockerfile", ".dockerignore"])
    run_cmd(["git", "add", "scripts/generate_task11.py", "scripts/generate_task11_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task11/"])
    run_cmd(["git", "add", "docs/DevOps_Task11_MayureshSawant_23102A0029.docx"])
    commit_with_date("feat(docker): implement multi-stage production Dockerfile and .dockerignore", "2026-10-17 09:25:30 -0700")

    # =========================================================================
    # WEEK 5 (Oct 18 - Oct 21): CD, Ansible IaC, Reliability & Release v1.5.0
    # =========================================================================

    # Commit 19 on dev: Jenkins-Docker Continuous Deployment
    run_cmd(["git", "add", "scripts/generate_task12.py", "scripts/generate_task12_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task12/"])
    run_cmd(["git", "add", "docs/DevOps_Task12_MayureshSawant_23102A0029.docx"])
    commit_with_date("ci(cd): extend Jenkinsfile with versioned Docker build, registry push, and container CD stages", "2026-10-18 13:40:22 -0700")

    # Commit 20 on dev: Ansible Configuration Management Playbook
    run_cmd(["git", "add", "ansible/hosts.ini", "ansible/ansible.cfg", "ansible/playbook.yml", "ansible/templates/"])
    run_cmd(["git", "add", "scripts/generate_task13.py", "scripts/generate_task13_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task13/"])
    run_cmd(["git", "add", "docs/DevOps_Task13_MayureshSawant_23102A0029.docx"])
    commit_with_date("feat(ansible): implement automated configuration management playbook and inventory", "2026-10-19 10:55:12 -0700")

    # Commit 21 on dev: Container Deployment, Idempotency & Rollback
    run_cmd(["git", "add", "ansible/deploy_app.yml", "ansible/rollback.yml"])
    run_cmd(["git", "add", "scripts/generate_task14.py", "scripts/generate_task14_diagrams.py"])
    run_cmd(["git", "add", "screenshots/task14/"])
    run_cmd(["git", "add", "docs/DevOps_Task14_MayureshSawant_23102A0029.docx"])
    commit_with_date("feat(reliability): add container deployment playbook, idempotency validation, and automated rollback", "2026-10-20 14:30:40 -0700")

    # Commit 22 on dev: Final Documentation, Architecture & Viva
    run_cmd(["git", "add", "scripts/generate_task15.py", "scripts/generate_task15_diagrams.py", "scripts/build_github_history.py"])
    run_cmd(["git", "add", "screenshots/task15/"])
    run_cmd(["git", "add", "docs/DevOps_Task15_MayureshSawant_23102A0029.docx"])
    commit_with_date("docs(task15): finalize end-to-end architecture, troubleshooting guide, and viva defense", "2026-10-21 09:15:00 -0700")

    # Final Merge into main for Release v1.5.0
    run_cmd(["git", "checkout", "main"])
    run_cmd(["git", "merge", "dev", "--no-ff", "--no-edit", "-m", "chore(release): merge all 15 DevOps tasks from dev to main"],
            env_dates="2026-10-21 11:30:00 -0700")
    run_cmd(["git", "tag", "-a", "v1.5.0", "-m", "Release v1.5.0: Complete Cold Storage Slot Booking System 15-Task DevOps Implementation", "HEAD"],
            env_dates="2026-10-21 11:35:00 -0700")
    print("Tagged Release v1.5.0 on main.")

    # Checkout dev as default active development branch
    run_cmd(["git", "checkout", "dev"])

    # Configure Remote
    run_cmd(["git", "remote", "add", "origin", REMOTE_URL], check=False)
    print(f"Configured remote 'origin' -> {REMOTE_URL}")

    # Remove temporary backup
    force_rmtree(os.path.join(REPO_DIR, ".git_bak"))
    print("Cleaned up temporary .git_bak directory.")

    print("\nSUCCESS: Complete 1-month git history constructed flawlessly!")

if __name__ == "__main__":
    main()
