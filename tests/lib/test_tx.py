import electrumx.lib.tx as tx_lib

tests = [
    "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1803e3810304c812a75c08810000e6020000007969696d70000000000006001bb700000000001976a914e8ba7124609206b563528a7c84b16803a87dccee88ac00512502000000001976a914ca80e2ef4d2c7246b4aa4d79a911f88a43d7d57f88ac00879303000000001976a9142a6564318d09a66d112a8eb116b6fd3511d5133688ac00093d00000000001976a9140670e62f36d5dda7e312b418cfe349643800dfa288ac00127a00000000001976a91490d8e1f871ab5cc03b0571c9ca42837a99f94a7b88ac0076b010000000001976a914159cf6ebb6ac1a3221e58342aa874974c6101faa88ac00000000"
]

def test_tx_serialiazation():
    for test in tests:
        test = bytes.fromhex(test)
        print ('------------------------------------------------------------------')
        print ('test : ',  test)
        deser = tx_lib.DeserializerZeon(test)
        tx = deser.read_tx()
        print ('------------------------------------------------------------------')
        print ('tx : ',  tx)
        assert tx.serialize() == test

if __name__ == "__main__":
    test_tx_serialiazation()
    print("Everything passed")

