from pywallet import wallet

def test_seed():
    seed = wallet.generate_mnemonic().split(' ')
    assert len(seed) == 12

def test_wallet():
    networks = [
        'btctest',
        'eth',
        'btc',
    ]
    seed = wallet.generate_mnemonic()
    for network in networks:
        w = wallet.create_wallet(network=network, seed=seed, children=1)
        assert isinstance(w, (dict))
        assert 'address' in w
        assert 'children' in w
        assert isinstance(w['children'], (list))

def test_children_walleet():
    networks = [
        'btctest',
        'eth',
        'btc',
    ]
    seed = wallet.generate_mnemonic()
    for network in networks:
        w = wallet.create_wallet(network=network, seed=seed, children=1)
        xpub_key = w['xpublic_key']
        address = wallet.create_address(network=network, xpub=xpub_key)
        assert isinstance(w, (dict))
        assert 'address' in address
        assert 'path' in address
