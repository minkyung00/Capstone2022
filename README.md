# π±2022 μΊ‘μ€ν€ νλ‘μ νΈπ±

μ΄λ¦°μ΄μ§ λ΄ μ€μκ° μλνλ μλ¦Ό μΉ μ¬μ΄νΈ

### λ°°ν¬ λ§ν¬: http://3.39.165.135/
 
## π οΈ κΈ°μ  μ€ν
- **Front-End** <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=flat&logo=Vue.js&logoColor=white"> <img src="https://img.shields.io/badge/NGINX-009639?style=flat&logo=NGINX&logoColor=white"> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=Bootstrap&logoColor=white">
- **Back-End** <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=Redis&logoColor=white"> <img src="https://img.shields.io/badge/Celery-37814A?style=flat&logo=Celery&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=SQLite&logoColor=white"><img src="https://img.shields.io/badge/Socket.io-010101?style=flat&logo=Socket.io&logoColor=white">
- **Deploy** <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/EC2-010101?style=flat&logo=EC2&logoColor=white"> <img src="https://img.shields.io/badge/AmazonS3-569A31?style=flat&logo=AmazonS3&logoColor=white">


 ## π νλ‘μ νΈ κ΅¬μ‘°
 
 ```bash
capstone2022
βββ backend               # λ°±μλ μ½λλ€
βββ frontend              # νλ‘ νΈμλ μ½λλ€
βββ docker-compose.yml    # λμ»€ μ»΄ν¬μ¦ νμΌ
βββ ...μ΄μΈ κΈ°ν νμΌλ€       # package.jsonμ λΉλ‘―ν κΈ°ν νμΌλ€
```

 ### Frontend κ΅¬μ‘°
 
 ```bash
frontend
βββ public                # index.html / favicon
βββ src
    βββ api               # api κ΄λ ¨ λͺ¨λλ€
    βββ assets            # νμν λ¦¬μμ€λ€
    βββ components        # μ»΄ν¬λνΈλ€
    βββ router            # λΌμ°ν°λ€
    βββ store             # μνκ΄λ¦¬
    βββ styles            # κ³΅ν΅ μ€νμΌλ€(base.scss)
    βββ utils             # μ¬μ¬μ© κ°λ₯ν λͺ¨λλ€
    βββ views             # νμ΄μ§λ€
    βββ App.vue(FILE)     # App μ»΄ν¬λνΈ
    βββ main.js(FILE)     # entry point
```

 ### Backend κ΅¬μ‘°
 
 ```bash
backend
βββ account               # κ³μ  κ΄λ ¨ app
βββ bin                   # μ€ν μ€ν¬λ¦½νΈ
βββ backend               # νκ²½λ³μ λ° μ€μ 
βββ center                # μ΄λ¦°μ΄μ§ κ΄λ ¨ app
βββ notification          # μλ¦Ό κ΄λ ¨ app
βββ utils                 # λ²μ© ν¨μ, ν΄λμ€λ€
βββ Dockerfile(FILE)      # λμ»€ νμΌ
βββ manage.py(FILE)       # command line μ νΈλ¦¬ν°
βββ requriements.txt(FILE)# μ€μΉ λͺ©λ‘
```

 ## βΆοΈ μ€μΉ λ° μ€ν
 
 ### νλ‘μ νΈ μ€μΉ λ° μ€ν - Development mode
 #### client
.env νμΌ
```bash
VUE_APP_API_URLT=YOUR SERVER API
 ```
 μ€ν
 ```bash
 npm install
 npm run serve
 ```
 
 ## π λ¬Έμ
