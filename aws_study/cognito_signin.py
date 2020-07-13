import boto3

def authenticate_and_get_token(username: str, password: str, app_client_id: str) -> None:
    client = boto3.client('cognito-idp')

    resp = client.initiate_auth(
        #UserPoolId=user_pool_id,
        ClientId=app_client_id,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password
#            "COMPANYID": "ingkle"
        }
    )

    print("Log in success")
    print("Access token:", resp['AuthenticationResult']['AccessToken'])
    print("ID token:", resp['AuthenticationResult']['IdToken'])
    #print("-"*100)
    #print("this is all result", resp['AuthenticationResult'])



if __name__ == "__main__":
    authenticate_and_get_token("ingkle.korea@gmail.com", "ingkle1",  "7makvn26ktugtskjc653nbrni7")
    
