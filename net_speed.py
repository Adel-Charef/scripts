import pyspeedtest


def main():
    speed_test = pyspeedtest.SpeedTest()
    download = f"Download Speed: {str(speed_test.download())} Bytes/second"
    upload = f"Upload Speed: {str(speed_test.upload())} Bytes/second"
    ping = f"Ping: {str(speed_test.ping())}"

    print(f"------{download}\n{upload}\n{ping}------")


if __name__ == "__main__":
    main()
