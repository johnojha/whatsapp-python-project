
from flask import Flask, jsonify, request
from flask_cors import CORS

import random
import http.client, urllib.parse, urllib.error, json

application = app = Flask(__name__)
CORS(app)

account_sid = 'AC320e696ec10b592a64bc614ffcf81c1c'
auth_token = '7b792eab5b495ae11ed31ba5bea398d8'



params = urllib.parse.urlencode({'bot': 'x1592563667910'})
headers = {
    'Content-Type': 'application/json',
    'x-auth-token': '83da4260b1f712337c2623ce60bd542cfb57a997b571f9b499679a19b0980ec3',
    'Host': 'app.yellowmessenger.com'
}


@app.route('/')
def index():
    return jsonify({
        'success': True,
        'message': 'This is index route!'
    })




@app.route('/sfmc/sendWhatsapp', methods=['POST'])
def send_whatsapp():
    if request.method == 'POST':
        try:
            received_data = request.get_json()
            print('Received Data', received_data)
            arguments = received_data.get('inArguments')

            number = arguments[0]['Phone']
            name = arguments[1]['Name']

            request_body = json.dumps({
                "body": {
                    "to": number,
                    "ttl": 200000,
                    "type": "template",
                    "template": {
                        "namespace": "95610748_ad07_4389_8b93_373d536063f0",
                        "language": {
                            "policy": "deterministic",
                            "code": "en"
                        },
                        "name": "precautionary_measures",
                        "components": [
                            {
                                "type": "header",
                                "parameters": [
                                    {
                                        "type": "image",
                                        "image": {
                                            "link": "https://emio.eclerx.com/whatsapp/covid.png"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            })

            conn = http.client.HTTPSConnection('app.yellowmessenger.com')
            conn.request("POST", "/integrations/whatsapp/send?%s" % params, body=request_body, headers=headers)
            response = conn.getresponse()
            response_data = json.loads(response.read().decode('ascii'))
            conn.close()

        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'something went wrong!'
            })

        return response_data



@app.route('/sfmc/sendWhatsapp1', methods=['POST'])
def send_whatsapp1():
    if request.method == 'POST':
        try:
            received_data = request.get_json()
            print('Received Data', received_data)
            arguments = received_data.get('inArguments')

            number = arguments[0]['Phone']
            name = arguments[1]['Name']

            request_body = json.dumps({
                "type": "media-notification",
                "mime": "image/png",
                "link": "https://cdn.vox-cdn.com/thumbor/FNRQapctOr2iQ9BA0EAlpNzwiQA=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/15788040/20150428-cloud-computing.0.1489222360.jpg",
                "body": {
                    "to": number,
                    "ttl": 200000,
                    "type": "template",
                    "template": {
                        "namespace": "95610748_ad07_4389_8b93_373d536063f0",
                        "language": {
                            "policy": "deterministic",
                            "code": "en"
                        },
                        "name": "ecx_drvaug",
                        "components": [
                            {
                                "type": "header",
                                "parameters": [
                                    {
                                        "type": "image",
                                        "image": {
                                            "link": "Plant.png"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            })

            conn = http.client.HTTPSConnection('app.yellowmessenger.com')
            conn.request("POST", "/integrations/whatsapp/send?%s" % params, body=request_body, headers=headers)
            response = conn.getresponse()
            response_data = json.loads(response.read().decode('ascii'))
            conn.close()

        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'something went wrong!'
            })

        return response_data



if __name__ == '__main__':
    app.run()
