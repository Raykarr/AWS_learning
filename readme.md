
---

## 📚 Project Documentation: Clarity Mirror

### 🔹 Overview

**Clarity Mirror** is a GenAI-powered reflection assistant built using open-source LLMs via [OpenRouter](https://openrouter.ai/), deployed on AWS EC2 with secure integrations to AWS S3 and IAM. The frontend is powered by Streamlit, allowing users to interact with the chatbot and store their reflections securely.

---

### 🧠 Features

* 🔒 **Secure Storage**: Reflections are uploaded to AWS S3.
* 📦 **LLM Integration**: Uses `deepseek/deepseek-r1-0528-qwen3-8b:free` via OpenRouter.
* 🛡️ **IAM Security**: Scoped-down IAM roles/policies for S3 and EC2 access.
* 🌐 **Deployed** on an EC2 Ubuntu instance with public access via port `8501`.
* 🔍 **Ready for OpenSearch** (optional - you can mention you’ve integrated or plan to integrate).
* 📊 **Future Monitoring**: Integrating CloudWatch for logs and metrics (optional).

---

### 🛠️ Tech Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Frontend         | Streamlit               |
| Backend LLM      | OpenRouter (DeepSeekR1) |
| Cloud Platform   | AWS (EC2, S3, IAM)      |
| Language         | Python                  |
| Deployment       | Ubuntu 22.04 on EC2     |
| Infra Monitoring | (Planned) CloudWatch    |
| Search           | (Optional) OpenSearch   |

---

### 🗂️ Project Structure

```bash
.
├── main.py              # Streamlit frontend + app logic
├── llm_handler.py       # Handles OpenRouter API calls
├── s3_uploader.py       # Uploads user thoughts to S3
├── config.json          # Stores OpenRouter key, S3 bucket name
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

### ⚙️ How to Run Locally

1. **Clone the Repo**

```bash
git clone https://github.com/your-username/cognitive-mirror.git
cd cognitive-mirror
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set Up `config.json`**

```json
{
  "openrouter_api_key": "your-key-here",
  "bucket_name": "your-s3-bucket",
  "region": "ap-south-1"
}
```

4. **Run Streamlit**

```bash
streamlit run main.py
```

---

### 🚀 AWS Deployment Instructions

**Instance**: `t2.micro` Ubuntu 22.04 (Free Tier)
**Ports to open**: `22 (SSH)`, `80 (HTTP)`, `443 (HTTPS)`, `8501 (Streamlit)`
**Security Group**: Custom TCP Rule for port `8501`
**File Transfer**: `scp -i key.pem cognitive-mirror.zip ubuntu@<EC2-PUBLIC-IP>:~/`

**Remote Setup**:

```bash
unzip cognitive-mirror.zip
cd cognitive-mirror
pip install -r requirements.txt
streamlit run main.py
```

---

### 🛡️ IAM Roles Used

* Created user `genai-user` with programmatic access.
* Applied scoped-down S3 policy allowing:

  * `s3:PutObject`
  * `s3:GetObject`
  * `s3:ListBucket`

**CLI Usage**:

```bash
aws configure
# Enter Access Key ID, Secret, Region: ap-south-1
```

---

### 📝 Future Improvements

* Add OpenSearch indexing
* Enable CloudWatch logs/alerts
* Add user login + session-based storage
* Save to RDS (PostgreSQL) instead of S3 (optional)

---

### 🧠 Prompt Engineering

To make the LLM more thoughtful:

```python
system_prompt = "You are a deep reflection assistant. Think from emotional, logical, social, and future consequences perspectives before giving suggestions."
```

---
