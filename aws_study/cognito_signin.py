def authenticate_and_get_token(username: str, password: str, 
                               user_pool_id: str, app_client_id: str) -> None:
    client = boto3.client('cognito-idp')

    resp = client.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=app_client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password
        }
    )

    print("Log in success")
    print("Access token:", resp['AuthenticationResult']['AccessToken'])
    print("ID token:", resp['AuthenticationResult']['IdToken'])

