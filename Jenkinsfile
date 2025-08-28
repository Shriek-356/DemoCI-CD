pipeline {
  agent any

  // === Cấu hình nhanh ===
  environment {
    REPO_URL        = 'https://github.com/Shriek-356/DemoCI-CD.git'
    BRANCH          = 'main'
    PY_VENV         = 'venv'  // tên thư mục venv cục bộ cho CI
    PY              = "venv\\Scripts\\python"
    PIP             = "venv\\Scripts\\pip"

    // ĐƯỜNG DẪN PROJECT & TEST
    REQUIREMENTS    = "MuonTraSach\\requirements.txt"
    TEST_DIR        = "MuonTraSach\\MuonTraSach\\tests"

    // DEPLOY (giống ví dụ bạn: copy .html sang IIS/wwwroot)
    DEPLOY_SRC      = "MuonTraSach\\MuonTraSach\\templates"
    DEPLOY_DST      = "D:\\wwwroot\\mysite"
    DEPLOY_PATTERN  = "*.html"   // muốn copy hết thì đổi thành "*.*"
  }

  stages {
    stage('Clone') {
      steps {
        // giống ví dụ của bạn
        git url: env.REPO_URL, branch: env.BRANCH
      }
    }

    stage('Setup & Install Requirements') {
      steps {
        bat """
          if exist %PY_VENV% rmdir /s /q %PY_VENV%
          python -m venv %PY_VENV%
          %PY% -m pip install --upgrade pip
          %PIP% install -r %REQUIREMENTS%
        """
      }
    }

    stage('Test') {
      steps {
        // unittest discover đơn giản (đổi pattern nếu cần)
        bat """
          %PY% -m unittest discover -s %TEST_DIR% -p "test_*.py" -v
        """
      }
    }

    stage('Build') {
      steps {
        echo 'Test thành công'
      }
    }

    stage('Deploy') {
      steps {
        // y hệt pattern xử lý mã thoát robocopy trong ví dụ của bạn
        bat """
          robocopy "%DEPLOY_SRC%" "%DEPLOY_DST%" %DEPLOY_PATTERN% /E /NFL /NDL /NJH /NJS /NP
          set RC=%%ERRORLEVEL%%
          if %%RC%% LEQ 3 ( exit /B 0 ) else ( exit /B %%RC%% )
        """
      }
    }
  }
}
