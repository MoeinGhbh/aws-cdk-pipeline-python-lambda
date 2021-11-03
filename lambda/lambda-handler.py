from botocore.exceptions import ClientError
import json,boto3,datetime
from geting_email_address import get_emails_address_cognito, all_email_address , update_emailaddress_db


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SteamKeys') 



def valid_steam_key():
    # lst_steam_key=[]
    response = table.scan()
    for h in  response['Items']:
        if h['steamkeyStatus'] == False:
           return  h['steamkeyValue'],h['steamkeysId']
    

def sent_emails_address():
    lst_steam_key=[]
    response = table.scan()
    for h in  response['Items']:
        if h['steamkeyStatus'] == True:
           lst_steam_key.append(h['email'])
    return lst_steam_key


def test():
    pass




def main(event, context):
    
    lst_sent_email_address = sent_emails_address()

    # this two below code remove the email address from the list that got the steam key
    emails_address = all_email_address()
    # emails_address = set(emails_address)-set(lst_sent_email_address)

            
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "inxspace@nexr-technologies.com"

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "eu-central-1"

    # The subject line for the email.
    SUBJECT = "NexR Show Invitation"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("This is a Nexr Show\r\n"
                 "This email was sent to handover your steam key "
                 "and you will get the newaletter from us."
                 )

    

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)
    
    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    for reciver in emails_address:
        # Try to send the email.
        try:
                    new_steamKey,steamkeysId = valid_steam_key()
                    print(new_steamKey,steamkeysId)
                    # The HTML body of the email.
                   
                    BODY_HTML = """
                    <!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style type="text/css">
        body {
            Margin: 0 !important;
            padding: 15px;
            background-color: #4A4A4A;
        }

        .wrapper {
            width: 100%;
            table-layout: fixed;
        }

        .wrapper-inner {
            width: 100%;
            background-color: #eee;
            max-width: 670px;
            Margin: 0 auto;
        }

        table {
            border-spacing: 0;
            font-family: sans-serif;
            color: #727f80;
        }

        .outer-table {
            width: 100%;
            max-width: 670px;
            margin: 0 auto;
            background-color: black;
        }

        td {
            padding: 0;
        }

        .header {
            background-color: #C2C1C1;
            border-bottom: 3px solid #81B9C3;
        }

        p {
            Margin: 0;
        }

        .header p {
            text-align: center;
            padding: 1%;
            font-weight: 500;
            font-size: 11px;
            text-transform: uppercase;
        }

        a {
            color: #F1F1F1;
            text-decoration: none;
        }

        /*--- End Outer Table 1 --*/
        .main-table-first {
            width: 100%;
            max-width: 610px;
            Margin: 0 auto;
            background-color: #FFF;
            border-radius: 6px;
            margin-top: 25px;
        }

        /*--- Start Two Column Sections --*/
        .two-column {
            text-align: center;
            font-size: 0;
            padding: 5px 0 10px 0;
        }

        .two-column .section {
            width: 100%;
            max-width: 300px;
            display: inline-block;
            vertical-align: top;
        }

        .two-column .content {
            font-size: 16px;
            line-height: 20px;
            text-align: justify;
        }

        .content {
            width: 100%;
            padding-top: 20px;
        }

        .center {
            display: table;
            Margin: 0 auto;
        }

        img {
            border: 0;
        }

        img.logo {
            float: left;
            Margin-left: 5%;
            max-width: 200px !important;
        }

        #callout {
            float: right;
            Margin: 4% 5% 2% 0;
            height: auto;
            overflow: hidden;
        }

        #callout img {
            max-width: 20px;
        }

        .social {
            list-style-type: none;
            Margin-top: 1%;
            padding: 0;
        }

        .social li {
            display: inline-block;
        }

        .social li img {
            max-width: 15px;
            Margin-bottom: 0;
            padding-bottom: 0;
        }

        /*--- Start Outer Table Banner Image, Text & Button --*/
        .image img {
            width: 100%;
            max-width: 670px;
            height: auto;
        }

        .main-table {
            width: 100%;
            max-width: 610px;
            margin: 0 auto;
            background-color: black;
            border-radius: 6px;
        }

        .one-column .inner-td {
            font-size: 16px;
            line-height: 20px;
            text-align: justify;
        }

        .inner-td {
            padding: 10px;
        }

        .h2 {
            text-align: center;
            font-size: 23px;
            font-weight: 600;
            line-height: 45px;
            Margin: 12px;
            color: #4A4A4A;
        }

        p.center {
            text-align: center;
            max-width: 580px;
            line-height: 24px;
        }

        .button-holder-center {
            text-align: center;
            Margin: 5% 2% 3% 0;
        }

        .button-holder {
            float: right;
            Margin: 5% 0 3% 0;
        }

        .btn {
            font-size: 15px;
            font-weight: 600;
            background: #81BAC6;
            color: #FFF;
            text-decoration: none;
            padding: 9px 16px;
            border-radius: 28px;
        }

        /*--- Start Two Column Image & Text Sections --*/
        .two-column img {
            width: 100%;
            max-width: 280px;
            height: auto;
        }

        .two-column .text {
            padding: 10px 0;
        }

        /*--- Start 3 Column Image & Text Section --*/
        .outer-table-2 {
            width: 100%;
            max-width: 670px;
            margin: 22px auto;
            background-color: #C2C1C1;
            border-bottom: 3px solid #81B9C3;
            border-top: 3px solid #81B9C3;
        }

        .three-column {
            text-align: center;
            font-size: 0;
            padding: 10px 0 30px 0;
        }

        .three-column .section {
            width: 100%;
            max-width: 200px;
            display: inline-block;
            vertical-align: top;
        }

        .three-column .content {
            font-size: 16px;
            line-height: 20px;
        }

        .three-column img {
            width: 100%;
            max-width: 125px;
            height: auto;
        }

        .outer-table-2 p {
            margin-top: 6px;
            color: rgb(51, 49, 49);
            font-size: 18px;
            font-weight: 500;
            line-height: 23px;
        }

        /*--- Start Two Column Article Section --*/
        .outer-table-3 {
            width: 100%;
            max-width: 670px;
            margin: 22px auto;
            background-color: #C2C1C1;
            border-top: 3px solid #81B9C3;
        }

        .h3 {
            text-align: center;
            font-size: 21px;
            font-weight: 600;
            Margin-bottom: 8px;
            color: #4A4A4A;
        }

        /*--- Start Bottom One Column Section --*/
        .inner-bottom {
            padding: 22px;
        }

        .h1 {
            text-align: center !important;
            font-size: 25px !important;
            font-weight: 600;
            line-height: 45px;
            Margin: 12px 0 20px 0;
            color: #4A4A4A;
        }

        .inner-bottom p {
            font-size: 16px;
            line-height: 24px;
            text-align: justify;
        }

        /*--- Start Footer Section --*/
        .footer {
            width: 100%;
            background-color: #C2C1C1;
            Margin: 0 auto;
            color: #FFF;
        }

        .footer img {
            max-width: 135px;
            Margin: 0 auto;
            display: block;
            padding: 4% 0 1% 0;
        }

        p.footer {
            text-align: center;
            color: #FFF !important;
            line-height: 30px;
            padding-bottom: 4%;
            text-transform: uppercase;
        }

        /*--- Media Queries --*/
        @media screen and (max-width: 400px) {
            .h1 {
                font-size: 22px;
            }

            .two-column .column,
            .three-column .column {
                max-width: 100% !important;
            }

            .two-column img {
                width: 100% !important;
            }

            .three-column img {
                max-width: 60% !important;
            }
        }

        @media screen and (min-width: 401px) and (max-width: 400px) {

            .two-column .column {
                max-width: 50% !important;
            }

            .three-column .column {
                max-width: 33% !important;
            }
        }

        @media screen and (max-width:768px) {
            img.logo {
                float: none !important;
                margin-left: 0% !important;
                max-width: 200px !important;
            }

            #callout {
                float: none !important;
                margin: 0% 0% 0% 0;
                height: auto;
                text-align: center;
                overflow: hidden;
            }

            #callout img {
                max-width: 26px !important;
            }

            .two-column .section {
                width: 100% !important;
                max-width: 100% !important;
                display: inline-block;
                vertical-align: top;
            }

            .two-column img {
                width: 100% !important;
                height: auto !important;
            }

            img.img-responsive {
                width: 100% !important;
                height: auto !important;
                max-width: 100% !important;
            }

            .content {
                width: 100%;
                padding-top: 0px !important;
            }

        }
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="wrapper-inner">
           

            
            <table class="main-table">
                <tr>
                    
                                        <td class="image">
                                            <a href="https://www.nexr-technologies.com/nexr-show/" target="_blank"><img
                                                    src="https://nexrbanner.s3.eu-central-1.amazonaws.com/nexr_banner_1.png"></a>
                                        </td>
                   
                </tr>
                <tr>
                    <td class="one-column">
                        <table width="100%">
                            <tr>
                                <td class="inner-td">
                                    <h1 style="color: rgb(237, 0, 86);text-align: center; letter-spacing: 20px;">THANK
                                        YOU!</h1>
                                    <p style="color: rgb(237, 0, 86);text-align: center;"> 
                                    FOR YOUR PARTICIPATION IN THE PAN-POT SHOW. 
                                        </p>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                    <p style="color: rgb(241, 241, 241);text-align: center;">
                                        PLEASE USE THIS STEAM KEY FOR DOWNLOADING NEXR SHOW
                                          </p>
                                        <br/>
                                        <br/>
  <p style="color: rgb(241, 241, 241);text-align: center;">
                                        Participant_steam_key
                                    </p>
                                    <br/>
                                    
                                    <p style="text-align: center;">
                                    
                                     <a href="https://nexrbanner.s3.eu-central-1.amazonaws.com/Steam_web_site.pdf"
                                                alt="this is button of user helper"
                                                style="font-size:20px;color: red;"> 
                                                
                                                                                    <button style=" background-color: #ed0056;
                                                                                      border: none;
                                                                                      color: white;
                                                                                      padding: 15px 32px;
                                                                                      text-align: center;
                                                                                      text-decoration: none;
                                                                                      display: inline-block;
                                                                                      font-size: 16px;
                                                                                      border-radius: 12px;">
                                                                                      
                                                                                Pan-Pot App download assistance for Steam  
                                                                        
                                                                        </button>
                                                                  </a>
                                      </p>
                                    

                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <!--- End Heading, Paragraph & Button Section -->
                <tr>
                    <td class="one-column">
                        <table width="100%">
                            <tr>
                                <td>
                                        <td class="image">
                                            <a href="https://www.nexr-technologies.com/nexr-show/" target="_blank">
                                            <img  src="https://nexrbanner.s3.eu-central-1.amazonaws.com/PanPot.png"></a>
                                        </td>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            <!--- End Heading, Paragraph & Button Section -->



            <tr>
                <td class="one-column">
                    <table width="100%">
                        <tr>
                            <td>
                                <p style="text-align: center;">
                                    <br>
                                    <a href="https://www.nexr-technologies.com/nexr-show/" alt=""> NexR Technologies
                                        company</a><br>

                                    <br>
                                    Contact:
                                    Charlottenstraße 4<br>
                                    10969 Berlin <br><br>
                                   
                                    E-Mail: inxspace@nexr-technologies.com
                                </p> <br>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>

        </div>
        <!--- End Wrapper Inner -->
      
    </div>
    <!--- End Wrapper -->
    <br>

</body>

</html>
                    """.replace('Participant_steam_key', new_steamKey)
                    # print(reciver)
                    # Provide the contents of the email.
                    response = client.send_email(
                                                    Destination={
                                                        'ToAddresses': [
                                                            reciver,
                                                        ],
                                                    },
                                                    Message={
                                                        'Body': {
                                                            'Html': {
                                                                'Charset': CHARSET,
                                                                'Data': BODY_HTML,
                                                            },
                                                            'Text': {
                                                                'Charset': CHARSET,
                                                                'Data': BODY_TEXT,
                                                            },
                                                        },
                                                        'Subject': {
                                                            'Charset': CHARSET,
                                                            'Data': SUBJECT,
                                                        },
                                                    },
                                                    Source=SENDER,
                                                 )
                    update_emailaddress_db(steamkeysId, reciver, table )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print('send email successfully')

    return {
        'statusCode': 200,
        'body': event
    }

