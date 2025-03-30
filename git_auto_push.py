import asyncio
import sys

async def run_command(command):
    process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

    return process.returncode

async def git_add():
    print("Adding Files...")
    return await run_command("git add .")

async def git_commit(message):
    print(f"Committing changes: {message}")
    return await run_command(f"git commit -m {message}")

async def git_push(branch="main"):
    print("Pushing to Github...")
    return await run_command("git push origin " + branch)

async def main():
    if len(sys.argv) < 2:
        print("Usage: python git_auto_push.py 'Your commit message'")
        return

    commit_message = sys.argv[1]

    if await git_add() == 0:
        if await git_commit(commit_message) == 0:
            await git_push()

if __name__ == "__main__":
    asyncio.run(main())
