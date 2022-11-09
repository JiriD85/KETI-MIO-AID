#
#	notificationServer.py
#
#	(c) 2020 by Andreas Kraft
#	License: BSD 3-Clause License. See the LICENSE file for further details.
#
#	Simple base implementation of a notification server to handle notifications 
#	from a CSE.
#

from __future__ import annotations
from http.client import HTTPMessage
from typing import cast
from http.server import HTTPServer, BaseHTTPRequestHandler
import email.parser
import json, argparse, sys, ssl, signal
import cbor2
from rich.console import Console
from rich.syntax import Syntax

import paho.mqtt.client as mqtt
import pathlib, os
parent = pathlib.Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(f'{parent}')
from acme.helpers.MQTTConnection import MQTTConnection, MQTTHandler
from acme.helpers.TextTools import toHex
from acme.etc.RequestUtils import serializeData
from acme.etc.DateUtils import getResourceDate
from acme.etc.Types import ContentSerializationType
from acme.etc.Constants import Constants as C

import ssl

##############################################################################
#
#	HTTP Server
#

port = 9999	# Change this variable to specify another port.
messageColor = 'spring_green2'
errorColor = 'red'

#Mqtt Values to publish to mosquitto
Broker="mqtt://mosquitto" 
Port =8883 
QOS = 1 
client=mqtt.Client()
# mqtt.tls_set(ca_certs=ca.crt, certfile=mio_aid.crt, keyfile=mio_aid.key, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
# TLS/SSL
ca_cert = "/var/lib/docker/volumes/acme_cseVolume/_data/tools/notificationServer/ca.crt"
certfile = "/var/lib/docker/volumes/acme_cseVolume/_data/tools/notificationServer/mio_aid.crt"
keyfile = "/var/lib/docker/volumes/acme_cseVolume/_data/tools/notificationServer/mio_aid.key"

 
actuatorStatusTrue={"fr":"aid","to":"/id-in/binSh4259115029833081984","op":3,"rvi":"3","rqi":"1234562","pc":{"cod:binSh":{"powSe":True}},"ty":28}
actuatorStatusFalse={"fr":"aid","to":"/id-in/binSh4259115029833081984","op":3,"rvi":"3","rqi":"1234562","pc":{"cod:binSh":{"powSe":False}},"ty":28} 
colorLedRed={"fr":"aid","to":"/id-in/binSh4259115029833081984","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":3,"sat":96,"x":0.6307692307692307,"y":0.3230769230769231,"colT":319}},"ty":28}
colorLedYellow={"fr":"aid","to":"/id-in/binSh4259115029833081984","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":66,"sat":93,"x":0.41847826086956524,"y":0.5054347826086957,"colT":255}},"ty":28}
colorLedDarkGreen={"fr":"aid","to":"/id-in/binSh4259115029833081984","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":104,"sat":93,"x":0.2962962962962963,"y":0.5925925925925926,"colT":250}},"ty":28}
colorLedOff={"fr":"aid","to":"/id-in/binSh4259115029833081984","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"powSe":False}},"ty":28}




topicActuatorStatus="/oneM2M/req/aqm/id-in/json"

client.tls_set(ca_certs=ca_cert, certfile=certfile, keyfile=keyfile, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
client.tls_insecure_set(True)
client.connect(Broker,Port)
#threshold values
co2Good = 800
co2Medium = 1000
co2Ok = 1400
tempHigh = 26
humidity = 0.6

failVerification = False

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self) -> None:
		"""	Just provide a simple web page.
		"""
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>[ACME] Notification Server</title></head><body>This server doesn't provide a web page.</body></html>","utf-8")) 


	def do_POST(self) -> None:
		"""	Handle notification.
		"""

		_responseHeaders:list = []

		# Get headers and content data
		length = int(self.headers['Content-Length'])
		contentType = self.headers['Content-Type']
		requestID = self.headers['X-M2M-RI']
		post_data = self.rfile.read(length)

		# Construct return header
		# Always acknowledge the verification requests
		self.send_response(200)
		self.send_header('X-M2M-RSC', '2000' if not failVerification else '4101')
		self.send_header('X-M2M-RI', requestID)
		_responseHeaders = self._headers_buffer	# type:ignore [attr-defined]
		self.end_headers()


		
		# Print the content data
		console.print(f'[{messageColor}]### Notification (http)')
		console.print(self.headers, highlight = False)

		###Automation Code ###
		y = json.loads(post_data)
		sensorCo2=float(y["m2m:sgn"]["nev"]["rep"]["mio:aiQSr"]["co2"])
		sensorHum=float(y["m2m:sgn"]["nev"]["rep"]["mio:aiQSr"]["hum"])
		sensorTemp=float(y["m2m:sgn"]["nev"]["rep"]["mio:aiQSr"]["temp"])

		if sensorCo2>co2Ok:
			print("Luft Qualität schlecht: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+"° " +"Hum: "+str(sensorHum)+"%")
			client.publish(topicActuatorStatus,json.dumps(actuatorStatusTrue),qos=QOS)
			client.publish(topicActuatorStatus,json.dumps(colorLedRed),qos=QOS)
		if co2Medium<sensorCo2<=co2Ok:
                	print("Luft Qualität ausreichend: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+"° " +"Hum: "+str(sensorHum)+"%")
                	client.publish(topicActuatorStatus,json.dumps(actuatorStatusFalse),qos=QOS)
#			client.publish(topicActuatorStatus,json.dumps(colorLedYellow),qos=QOS)
		if co2Medium<sensorCo2<=co2Ok:
                	print("Luft Qualität ausreichend: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+"° " +"Hum: "+str(sensorHum)+"%")
                	client.publish(topicActuatorStatus,json.dumps(actuatorStatusFalse),qos=QOS)
                	client.publish(topicActuatorStatus,json.dumps(colorLedDarkGreen),qos=QOS)
		###End of Automation###

		# Print JSON
		if contentType in [ 'application/json', 'application/vnd.onem2m-res+json' ]:
			console.print(Syntax(json.dumps(json.loads(post_data.decode('utf-8')), indent=4),
							 'json', 
							 theme='monokai',
							 line_numbers=False))
		
		# Print CBOR
		elif contentType in [ 'application/cbor', 'application/vnd.onem2m-res+cbor' ]:
			console.print('[dim]Content as Hexdump:\n')
			console.print(toHex(post_data), highlight=False)
			console.print('\n[dim]Content as JSON:\n')
			console.print(Syntax(json.dumps(cbor2.loads(post_data), indent=4),
							 'json', 
							 theme='monokai',
							 line_numbers=False))		

		# Print other binary content
		else:
			console.print(toHex(post_data), highlight=False)
		
		# Print HTTP Response
		# This looks a it more complicated but is necessary to render nicely in Jupyter
		console.print(f'[{messageColor}]### Notification Response (http)')
		console.print(email.parser.Parser(_class = HTTPMessage).parsestr(b''.join(_responseHeaders).decode('iso-8859-1')), highlight = False)


	def log_message(self, format:str, *args:int) -> None:
		if (msg := format%args).startswith('"GET'):	return	# ignore GET log messages
		console.print(f'[{messageColor} reverse]{msg}', highlight = False)


##############################################################################
#
#	MQTT Client
#

mqttNotificationTopic = [ '/oneM2M/req/id-in/+/#' ]

class MQTTClientHandler(MQTTHandler):

	def __init__(self, topic:str|list[str], enableLogging:bool) -> None:
		super().__init__()
		self.topic = topic
		self.enableLogging = enableLogging
		self.isShutdown = False


	def onConnect(self, connection:MQTTConnection) -> bool:
		try:
			connection.subscribeTopic(self.topic, self._requestCB)					# Subscribe to general requests
		except Exception as e:
			self.onError(connection, -1, f'MQTT {str(e)}')
		return True


	def onError(self, connection:MQTTConnection, rc:int=-1, msg:str=None) -> bool:
		if rc in [5]:		# authorization error
			console.print(f'[{errorColor}]MQTT authorization error')
			connection.shutdown()
			console.print(f'[{messageColor}]MQTT client shutdown')
		if rc == -1: 	# unknown. probably connection error?
			if msg:
				console.print(f'[{errorColor}]{msg}')
			connection.shutdown()
			console.print(f'[{messageColor}]MQTT client shutdown')
		# ignore all others
		return True


	def logging(self, connection:MQTTConnection, level:int, message:str) -> bool:
		if self.enableLogging:
			console.print(f'{level}: {message}')
		return True


	def onShutdown(self, connection: MQTTConnection) -> None:
		if not self.isShutdown:
			os.kill(os.getpid(), signal.SIGUSR1)
	

	def _requestCB(self, connection:MQTTConnection, topic:str, data:bytes) -> None:
		# TODO is it actually a notification? no -> do nothing, yes -> reply

		def _constructResponse(frm:str, to:str, jsn:dict) -> dict:
			responseData = 	{ 	'fr':	frm,
								'to':	to, 
								'rsc':	2000 if not failVerification else 4101,
								'ot':	getResourceDate()
							}
			if (rqi := jsn.get('rqi')):
				responseData['rqi'] = rqi
			if (rvi := jsn.get('rvi')):
				responseData['rvi'] = rvi
			return responseData


		console.print(f'[{messageColor}]### Notification (MQTT)')
		console.print(f'Topic: {topic}')
		topicArray	= topic.split('/')
		if len(topicArray) > 4 and topicArray[-4] == 'req' and topicArray[-5] == 'oneM2M':
			_frm		= topicArray[-3]
			_to			= topicArray[-2]
			encoding	= topicArray[-1]
		else:
			_frm 		= 'non-onem2m-entity'	
			_to 		= 'unknown'
			encoding	= 'json'

		# Print JSON
		responseData = None
		if encoding.upper() == 'JSON':
			console.print(Syntax(json.dumps((jsn := json.loads(data)), indent=4),
							 'json', 
							 theme='monokai',
							 line_numbers=False))
			to 	= jsn['to'] if 'to' in jsn else _to
			frm = jsn['fr'] if 'fr' in jsn else _frm
			responseData = cast(bytes, serializeData(_constructResponse(to, frm, jsn), ContentSerializationType.JSON))
			console.print(responseData)



		# Print CBOR
		elif encoding.upper() == 'CBOR':
			console.print('[dim]Content as Hexdump:\n')
			console.print(toHex(data), highlight=False)
			console.print('\n[dim]Content as JSON:\n')
			console.print(Syntax(json.dumps((jsn := cbor2.loads(data)), indent=4),
							 'json', 
							 theme='monokai',
							 line_numbers=False))		
			to 	= jsn['to'] if 'to' in jsn else to
			frm = jsn['fr'] if 'fr' in jsn else frm
			responseData = cast(bytes, serializeData(_constructResponse(to, frm, jsn), ContentSerializationType.CBOR))

		# Print other binary content
		else:
			console.print('[dim]Content as Hexdump:\n')
			console.print(toHex(data), highlight=False)
		# TODO send a response

		if responseData:
			# connection.publish(f'/oneM2M/resp{frm}/{to.lstrip("/").replace("/", ":")}/{encoding}', responseData)
			connection.publish(f'/oneM2M/resp/{_frm}/{_to}/{encoding}', responseData)


class MQTTClient(object):

	def __init__(self, args:argparse.Namespace) -> None:
		# Assume a couple of meaningful defaults here
		self.mqttConnection = MQTTConnection(address			= args.mqttAddress,
											 port				= args.mqttPort,
											 keepalive			= 60,
											 interface			= '0.0.0.0',
											 username 			= args.mqttUsername,
											 password			= args.mqttPassword,
											 messageHandler 	= MQTTClientHandler	(args.mqttTopic, args.mqttLogging))
	

	def run(self) -> None:
		self.mqttConnection.run()
		console.print(f'[{messageColor}]MQTT client started. Connected to {args.mqttAddress}:{args.mqttPort}.')
	

	def shutdown(self) -> None:
		self.mqttConnection.messageHandler.isShutdown = True	# type:ignore [attr-defined]
		if self.mqttConnection:
			self.mqttConnection.shutdown()
			console.print(f'[{messageColor}]MQTT client stopped.')
	
##############################################################################

#
#	Help with exiting and terminating all the threads programmatically
#	
class ExitCommand(Exception):
	pass

def exitSignalHandler(signal, frame) -> None:	# type: ignore [no-untyped-def]
	raise ExitCommand()

def exitAll() -> None:
	os.kill(os.getpid(), signal.SIGUSR1)

signal.signal(signal.SIGUSR1, exitSignalHandler)
	
if __name__ == '__main__':
	console = Console()
	console.print(f'\n{C.textLogo} - [bold]Notification Server[/bold]\n\n')


	# parse command line argiments
	parser = argparse.ArgumentParser()

	# mutual exlcusive arguments for http
	groupHttp = parser.add_mutually_exclusive_group()
	groupHttp.add_argument('--http', action='store_false', dest='usehttps', default=None, help='run as http server (the default)')
	groupHttp.add_argument('--https', action='store_true', dest='usehttps', default=None, help='run as https server')
	parser.add_argument('--port', action='store', dest='port', default=port, type=int, help='specify the server port')
	parser.add_argument('--certfile', action='store', dest='certfile', required='--https' in sys.argv, metavar='<filename>', help='specify the certificate file for https')
	parser.add_argument('--keyfile', action='store', dest='keyfile', required='--https' in sys.argv, metavar='<filename>', 	help='specify the key file for https')

	# MQTT arguments
	parser.add_argument('--mqtt', action='store_true', dest='mqtt', default=False, help='enable MQTT for notifications')
	parser.add_argument('--mqtt-address', action='store', dest='mqttAddress', default='localhost', required='--mqtt' in sys.argv, metavar='<host>', help='MQTT broker address (default: localhost)')
	parser.add_argument('--mqtt-port', action='store', dest='mqttPort', default=1883, metavar='<port>',  help='MQTT broker port (default: 1883)')
	parser.add_argument('--mqtt-topic', action='store', dest='mqttTopic', default=mqttNotificationTopic, metavar='<topic>', nargs='+', help=f'MQTT topic list (default: {mqttNotificationTopic})')
	parser.add_argument('--mqtt-username', action='store', dest='mqttUsername', default=None, metavar='<username>',  help='MQTT username (default: None)')
	parser.add_argument('--mqtt-password', action='store', dest='mqttPassword', default=None, required='--mqttUsername' in sys.argv, metavar='<password>',  help='MQTT password (default: None)')
	parser.add_argument('--mqtt-logging', action='store_true', dest='mqttLogging', default=False, help='MQTT enable logging (default: disabled)')

	# Generic
	parser.add_argument('--fail-verification', action='store_true', dest='failVerification', default=False, help='Fail verification requests (default: false)')



	args = parser.parse_args()

	# Generic arguments
	failVerification = args.failVerification

	# run http(s) server
	httpd = HTTPServer(('', args.port), SimpleHTTPRequestHandler)
	
	if args.usehttps:
		# init ssl socket
		context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)					# Create a SSL Context
		context.load_cert_chain(args.certfile, args.keyfile)				# Load the certificate and private key
		httpd.socket = context.wrap_socket(httpd.socket, server_side=True)	# wrap the original http server socket as an SSL/TLS socket
	
	console.print(f'[{messageColor}]Notification server started.')
	try:
		# run mqtt client
		mqttClient = None
		if args.mqtt:
			mqttClient = MQTTClient(args)
			mqttClient.run()

		# run http server
		console.print(f'[{messageColor}]Listening for http(s) connections on port {args.port}.')
		httpd.serve_forever()
	except KeyboardInterrupt as e:
		if mqttClient:
			mqttClient.shutdown()
		# The http server is stopped implicitly
	except ExitCommand:
		pass
	except Exception:
		console.print()
		console.print_exception()
	finally:
		console.print(f'[{messageColor}]Notification server stopped.')

