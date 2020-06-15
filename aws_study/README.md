# aws cognito
    aws cognito는 UserPool 안에서 적당한 접근 권한을 주기 위해 사용하는 서비스(회원가입 및 로그인 등등)
    appsync와 같은 api를 찌를때 x-api-key로 찔러도 되지만, key가 외부로 노출되어있고, 스키마를 아는 사람이라면 
    DB를 악의적으로 조작하는게 가능 할 수 있음. 따라서 cognito 인증을 받아 JWT토큰을 얻어서(유효기간 최대 1시간)
    이를 토대로 api를 찌르는 것이 보안에 유리
