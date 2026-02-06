# 🐙 UPLOAD FACTORY TO GITHUB

> **How to share your Mobile Factory Unit**

## Option A: New Repository (Share the Factory)
Use this if you want to share the factory tools with others.

1.  **Initialize Git**:
    ```bash
    cd _factory_dist
    git init
    ```

2.  **Commit Files**:
    ```bash
    git add .
    git commit -m "Initial commit: Antigravity Mobile Factory"
    ```

3.  **Push to GitHub**:
    *   Create a new repository on GitHub (e.g., `my-ai-factory`).
    *   Run the commands shown by GitHub:
    ```bash
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/my-ai-factory.git
    git push -u origin main
    ```

---

## Option B: Add to Existing Project
Use this if you want to commit the factory *inside* your game project.

1.  **Move Files**:
    Ensure the `.agent` folder (extracted from zip) is in your project root.

2.  **Update .gitignore**:
    Add these lines to your project's `.gitignore` to keep the factory clean:
    ```text
    .agent/*.log
    .agent/*.pid
    .agent/tmp/
    ```

3.  **Commit**:
    ```bash
    git add .agent
    git commit -m "chore: Install Antigravity Factory"
    git push
    ```

## 🔄 How to Update
To update the factory later:
1.  Download the new `antigravity-factory.zip`.
2.  Replace the old file in your repo.
3.  Commit and push: `git commit -am "update: Factory Core v2.0"`
