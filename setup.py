from setuptools import setup

setup(
    name="electrum-ppc-server",
    version="0.9",
    scripts=['run_electrum_ppc_server','electrum-ppc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumppcserver':'src'
        },
    py_modules=[
        'electrumppcserver.__init__',
        'electrumppcserver.utils',
        'electrumppcserver.storage',
        'electrumppcserver.deserialize',
        'electrumppcserver.networks',
        'electrumppcserver.blockchain_processor',
        'electrumppcserver.server_processor',
        'electrumppcserver.processor',
        'electrumppcserver.version',
        'electrumppcserver.ircthread',
        'electrumppcserver.stratum_tcp',
        'electrumppcserver.stratum_http'
    ],
    description="Peercoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/testalt/electrum-server/",
    long_description="""Server for the Electrum Lightweight Peercoin Wallet"""
)


