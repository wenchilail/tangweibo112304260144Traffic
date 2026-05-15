# GitHub上传指南

## 已完成的工作

✅ 项目结构已搭建完成
```
交通标志检测/
├── code/              # 实验代码
│   ├── baseline_infer.py
│   ├── data.yaml
│   ├── run_infer.py
│   ├── train.py
│   └── train_model.py
├── report/            # 实验报告
│   └── 第四次实验报告.md
├── results/           # 实验结果
│   ├── BoxPR_curve.png
│   ├── confusion_matrix.png
│   ├── results.csv
│   └── results.png
├── .gitignore         # Git忽略文件配置
└── README.md          # 项目说明文档
```

✅ Git仓库已初始化
✅ 所有需要的文件已添加到暂存区

## 下一步操作

### 1. 在GitHub上创建仓库
1. 登录 https://github.com
2. 点击右上角的 "+" -> "New repository"
3. 仓库名称可以设置为：`traffic-sign-detection` 或其他你喜欢的名字
4. 选择 Public 或 Private（根据课程要求）
5. **不要**勾选 "Initialize this repository with a README"
6. 点击 "Create repository"

### 2. 配置Git用户信息（在PowerShell中执行）

```powershell
# 进入项目目录
cd "d:\Trae programes\交通标志检测"

# 配置你的GitHub用户名和邮箱（替换成你自己的）
git config user.name "你的GitHub用户名"
git config user.email "你的GitHub邮箱"

# 提交更改
git commit -m "初始化: 完成第四次交通标志检测实验"
```

### 3. 推送到GitHub

```powershell
# 关联远程仓库（替换成你自己的仓库地址）
git remote add origin https://github.com/你的用户名/你的仓库名.git

# 重命名分支为main（如果需要）
git branch -M main

# 推送到GitHub
git push -u origin main
```

### 4. 如果是首次使用Git，可能需要身份验证

如果提示需要登录，可以使用以下方法之一：
- 使用GitHub Personal Access Token
- 使用GitHub Desktop图形界面工具

### 5. 创建Personal Access Token（如果需要）

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token" -> "Generate new token (classic)"
3. 设置Expiration（过期时间）
4. 勾选 `repo` 权限
5. 点击 "Generate token"
6. 复制生成的token（只显示一次！）
7. 当git push提示输入密码时，粘贴这个token

## 验证上传成功

完成后，在GitHub上刷新你的仓库页面，应该能看到：
- code/ 目录
- report/ 目录
- results/ 目录
- README.md
- .gitignore

## 后续实验更新

每次完成新的实验后，执行以下步骤：

```powershell
# 查看修改
git status

# 添加修改
git add .

# 提交修改（写清楚提交说明）
git commit -m "第五次实验: xxx"

# 推送到GitHub
git push
```

## 实验回退

如果需要回退到之前的版本：

```powershell
# 查看历史提交
git log

# 回退到某个版本（保留修改）
git reset --soft <commit-id>

# 回退到某个版本（丢弃修改）
git reset --hard <commit-id>
```

## 比赛提交说明

比赛提交文件位于：
`第4次实验数据及提交格式/submission.csv`

这个文件不需要上传到GitHub（已在.gitignore中配置），直接提交到比赛平台即可。

## 注意事项

1. **不要**上传数据集文件（train/、val/、test/）
2. **不要**上传大的模型文件（.pt、.pth等）
3. 每次提交说明要清晰明确
4. 及时提交，不要等最后一次才提交
