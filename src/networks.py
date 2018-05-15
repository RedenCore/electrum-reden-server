# Main network and testnet3 definitions

# Reden src/chainparams.cpp
params = {
    'reden_main': {
        'pubkey_address': 76, #L120
        'script_address': 16, #L122
        'genesis_hash': '00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6' #L110
    },
    'reden_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #L210
    }
}
