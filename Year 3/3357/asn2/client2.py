from chatroom import ClientUDP
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', type=str, help='Client name')
args = parser.parse_args()
client = ClientUDP("Alli", 12345)
client.run()
client.send("")