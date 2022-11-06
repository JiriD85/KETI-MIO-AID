## Set up CA with OpenSSL ##

### Generate Keys and Certificate Signing Request (CSR) ###

With the provided configuration file *mio_aid.conf* we can create a CSR with the proper extensions.

Command:
```
openssl req -new -out mio_aid.csr -config mio_aid.conf
```

Creation of the key in shell:
```
Generating a RSA private key
.............................++++
....++++
writing new private key to 'mio_aid.key'
-----
```

OpenSSL uses the information from our configuration file to create the CSR and a key-file *mio_aid.key*

Command:
```
openssl req -in mio_aid.csr -noout -text
```

Result:
```
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: C = AT, ST = Vienna, L = Vienna, O = MIO_AID, CN = localhost
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (4096 bit)
                Modulus:
                    00:aa:0f:4e:03:10:4a:80:df:d8:55:94:ad:01:a3:
                    ac:3f:ca:f3:24:a8:2c:0c:4d:ee:5c:9d:ba:d8:25:
                    ba:d9:4d:50:75:8c:1f:fc:95:51:fb:a9:d7:93:00:
                    06:84:6e:b0:af:ad:9c:d5:c0:63:fb:f5:b5:12:fb:
                    85:12:37:c8:6b:96:30:78:f2:16:88:b8:31:c1:f1:
                    aa:1d:4c:bf:d1:a6:a2:6c:39:87:be:93:f4:46:c2:
                    79:f2:13:4a:ab:e3:82:68:b3:e8:a5:d1:53:ec:0d:
                    33:fc:11:53:11:3c:3f:83:ff:20:fc:f2:1c:d8:38:
                    83:c2:94:83:14:a7:ba:0c:75:d0:eb:fb:d5:1a:f6:
                    6a:bd:c0:0f:ae:88:31:d4:2e:83:ae:fd:1c:b8:93:
                    b3:eb:87:14:82:36:ec:c0:39:3d:79:33:47:9f:5a:
                    6e:7a:cf:4d:00:fb:9d:29:e4:49:31:ad:ea:32:27:
                    a0:ce:df:d9:88:fd:21:75:59:d4:2c:df:ff:e5:fc:
                    ae:75:01:6b:11:90:b3:ba:77:4e:e5:cf:09:7f:b7:
                    ed:96:65:66:49:ee:d1:8c:81:92:c3:77:f1:ca:56:
                    b8:09:08:5c:ab:ba:ca:3e:97:82:50:51:c6:84:13:
                    06:36:64:38:1b:5f:50:18:7a:6f:98:a3:38:c1:e1:
                    f3:af:81:b7:c6:38:83:47:c9:87:bb:db:c8:59:b5:
                    cd:51:af:a4:3a:22:fa:9f:fd:d5:cd:ce:92:50:9c:
                    e0:3f:a6:06:f8:0b:1a:28:e9:a6:61:a6:ae:14:f3:
                    92:03:b4:25:57:dd:f5:90:58:f7:20:51:1d:3f:2d:
                    5d:74:f5:b9:94:79:03:e8:fd:a3:f8:c8:86:9d:1a:
                    04:2d:10:6c:a9:8f:ca:6d:37:f6:f3:3b:63:44:d7:
                    21:b7:a2:4f:83:ac:85:fd:31:7c:88:45:4d:7d:ee:
                    42:4b:fb:9c:bf:8e:8c:2d:e9:c5:66:57:32:38:29:
                    7b:df:ea:16:31:60:ba:33:0b:26:5f:92:e0:e9:e5:
                    09:62:9c:0c:9f:a5:ca:58:7e:78:bb:09:dc:9a:d0:
                    fb:90:eb:1a:3e:61:5e:d6:5d:a9:b7:0a:8a:66:ac:
                    d7:b3:12:9e:91:d3:a3:fa:8a:88:a4:55:12:7f:32:
                    48:17:2e:c5:57:f6:77:e8:4a:8b:c6:3b:56:42:c7:
                    63:43:8d:80:b4:4e:2f:37:5b:24:f5:c1:dd:e0:88:
                    73:dd:8b:d8:3a:d1:ac:d2:ff:a1:5a:43:04:37:0a:
                    96:17:ec:ec:67:e4:54:13:8e:58:5c:c4:d0:f0:e7:
                    85:86:31:fb:e8:3a:a2:0a:2b:c2:1b:9e:9b:60:d0:
                    7b:ef:f1
                Exponent: 65537 (0x10001)
        Attributes:
        Requested Extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Alternative Name:
                DNS:mosquitto, DNS:cse, DNS:zigbeem2qtt, DNS:nodered, DNS:grafana, DNS:portainer
            X509v3 Subject Key Identifier:
                2E:53:4E:0B:45:90:E7:62:A8:60:46:61:BF:6B:5E:E7:AB:7F:72:00
    Signature Algorithm: sha1WithRSAEncryption
         8c:71:c9:4a:55:93:c1:71:b7:5d:c6:6a:2c:19:6c:d4:22:c2:
         ef:59:1a:1e:e8:02:e7:f2:1a:a9:8e:07:80:fb:5e:7b:13:75:
         d7:c3:c3:d3:dc:35:8d:55:db:19:90:a3:05:94:71:b9:ad:d8:
         cd:24:f5:3e:35:02:05:cb:4e:45:a1:76:5a:a3:cf:b6:56:fc:
         0a:11:9b:5f:7c:d0:e1:32:26:e3:42:0e:b2:8e:fa:f9:d3:29:
         0d:4e:a2:ec:18:06:0d:35:65:e8:85:62:16:92:1b:70:10:6e:
         fa:fd:ab:86:1a:27:5c:ae:30:2e:1d:17:55:18:0d:59:05:c0:
         d0:c2:6b:d0:3e:88:2e:ae:e4:91:29:0b:c3:4e:c4:c6:fd:27:
         79:66:93:c4:5e:e1:6b:49:df:60:ff:81:3d:30:34:d7:86:be:
         88:f4:94:1f:77:c2:78:c9:1e:21:b1:13:43:fa:85:cc:82:73:
         d1:16:63:7c:53:7e:54:a4:7f:d8:4b:c3:3c:3d:2e:ac:53:4f:
         51:5e:09:c0:32:8e:2f:71:7d:66:db:6f:92:74:4b:54:58:f1:
         c6:a8:de:c8:4e:61:03:59:8c:18:56:16:ae:cb:43:08:96:84:
         65:c0:8e:56:8a:96:0a:2f:ec:87:42:8b:9b:9b:33:5f:2e:14:
         cc:5e:be:ad:10:04:70:03:95:c2:91:f8:86:f8:72:f4:55:b8:
         66:43:9b:3b:9d:c1:6f:c7:2f:b2:af:bc:47:0d:4b:a7:19:2f:
         f6:78:99:71:02:29:7d:dd:c2:6a:22:d8:d0:51:c0:d9:ae:8a:
         fd:63:f0:88:cf:50:d9:ff:25:3e:4f:7f:a7:9b:bd:73:8b:84:
         d9:cc:1a:0f:b1:37:f8:b3:8d:50:b4:98:f8:d0:d7:e9:04:80:
         22:11:20:8a:56:b5:f9:4d:8a:c3:36:b8:eb:46:ba:46:08:0b:
         b9:6e:df:8e:8b:90:6e:1f:08:1e:09:91:d5:46:37:bb:7f:39:
         b8:94:d4:14:8a:fb:1e:9e:f2:ec:46:b8:97:5a:f9:c8:d6:28:
         05:b5:a8:7f:09:a1:fa:67:36:1a:02:e6:9f:c6:62:ff:7b:d5:
         51:b4:0a:77:07:6d:90:97:d9:55:a3:7e:55:dc:e3:90:55:14:
         a6:a3:2a:06:0c:f8:64:9e:63:c9:51:30:4e:14:5a:40:d8:8a:
         12:b3:ba:6a:b7:a9:31:31:f2:35:72:b5:03:31:50:46:86:be:
         dc:94:65:e7:07:46:ec:0b:de:df:2e:6f:ea:55:23:1f:73:c5:
         b7:0e:88:a5:f2:cf:5a:69:3e:7e:f9:5a:59:f6:06:4d:ac:d5:
         8d:42:63:b5:0a:45:72:c3
```

### CA key and self-signed Certificate ###
Generate a key for the subject:
```
openssl genrsa -out ca.key 4096
```

Generate a self signed certificate for the CA:
```
openssl req -new -x509 -key ca.key -out ca.crt
```

The configuration file *ca.conf* provides the settings for our CA. 
We need to setup a strucuture first. Our configuration file expects a directory *newcerts*, a the files *index.txt* and *serial*
```
mkdir newcerts
touch index.txt
echo '01' > serial
```

Now we can sign our certificates with the CA:
```
openssl ca -config ca.conf -out mio_aid.crt -infiles mio_aid.csr
```

Signing and commiting:
```
Using configuration from ca.conf
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
countryName           :PRINTABLE:'AT'
stateOrProvinceName   :ASN.1 12:'Vienna'
localityName          :ASN.1 12:'Vienna'
organizationName      :ASN.1 12:'MIO_AID'
commonName            :ASN.1 12:'localhost'
Certificate is to be certified until Nov  6 20:21:22 2023 GMT (365 days)
Sign the certificate? [y/n]:y


1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
```

If we wish to add extensions, then we need to include the configuration file *mio_aid.extensions.conf*:
```
openssl ca -config ca.conf -out mio_aid.crt -extfile mio_aid.extensions.conf -in mio_aid.csr
```

Now we have a certificate that includes SubjectAltNames:
```
openssl x509 -in mio_aid.crt -noout -text

```

Output:
```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 1 (0x1)
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: C = AT, ST = Vienna, L = Vienna, O = MIO_AID, CN = localhost
        Validity
            Not Before: Nov  6 20:54:15 2022 GMT
            Not After : Nov  6 20:54:15 2023 GMT
        Subject: C = AT, ST = Vienna, O = MIO_AID, CN = localhost
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (4096 bit)
                Modulus:
                    00:b4:8d:39:39:ad:b7:fa:7e:36:78:f6:a1:20:66:
                    56:0b:05:64:09:71:87:df:f4:6e:4f:b8:e2:d4:c8:
                    ef:ab:56:dd:2b:a5:f5:e1:bc:1e:10:93:f1:59:e5:
                    1c:bd:eb:0e:26:29:33:e7:1b:2d:79:4e:13:63:58:
                    34:7f:e5:56:0a:68:24:5b:3e:26:67:0f:29:6e:4b:
                    4a:38:68:37:b9:30:8e:f1:31:c5:9e:4e:cf:08:9d:
                    66:8a:a5:9c:b4:10:95:53:8f:6c:14:d6:9b:0d:2e:
                    bc:5e:d8:ed:9e:87:b3:f1:9e:24:8a:1c:dd:71:ea:
                    0b:60:00:02:73:bc:90:3d:b3:81:c8:8a:0e:c6:67:
                    72:9f:93:4e:7e:a6:97:f0:06:77:c0:06:bb:48:b0:
                    a9:1b:47:df:a3:9e:a1:0d:7a:62:8f:86:55:a6:88:
                    af:ad:2a:d4:72:5d:db:28:43:07:4a:84:5d:79:f6:
                    5f:8d:26:03:25:05:ea:2b:85:fd:23:3a:47:cc:96:
                    44:16:16:cf:fc:64:c1:77:cf:30:6b:13:9a:b9:74:
                    26:b5:27:ef:92:00:46:ff:96:31:56:d6:16:54:cd:
                    26:4c:96:e8:fe:5f:47:22:a1:8d:a9:f3:14:3c:38:
                    07:08:e4:25:c2:99:5d:b2:d7:b8:b9:89:5d:81:f1:
                    08:2d:66:52:18:51:a9:0a:a3:d6:ca:50:d4:1f:50:
                    34:2f:5f:d2:2e:3d:af:07:d4:83:53:6c:0d:60:ac:
                    e1:2e:72:4f:b6:62:81:16:36:c7:65:d4:59:19:cf:
                    89:cd:50:f7:36:31:bb:96:c5:2d:13:dc:4e:c6:4b:
                    9b:dd:0f:23:2c:9e:34:30:71:e3:6c:ab:c5:7b:52:
                    be:77:93:18:c2:5d:65:de:85:79:ac:18:3c:c5:6b:
                    ef:20:0a:a8:16:a5:9a:2d:b3:22:10:63:74:5e:49:
                    2d:18:0a:14:ac:65:81:b9:0c:cd:75:a0:91:c8:a3:
                    b9:53:69:21:e7:22:a0:5d:c4:f5:f6:39:d5:40:9b:
                    b2:9b:e2:00:bb:85:04:e3:ed:82:c9:d7:f9:32:5f:
                    51:05:38:5f:9e:1a:d8:bb:4e:70:f9:ff:ab:df:d3:
                    96:a9:04:02:90:c7:d2:30:a3:f3:70:58:29:42:16:
                    66:e1:48:df:98:32:86:ea:aa:69:a0:49:76:f0:8a:
                    b2:ad:5f:a4:a0:fb:38:86:8e:f9:4a:38:2d:d3:1d:
                    33:1e:6c:14:0f:ef:8d:f1:e7:78:11:14:e3:70:89:
                    10:96:6d:f2:9f:fd:c9:2c:e0:8e:a2:89:91:b9:d1:
                    58:5c:96:4d:00:58:bb:97:98:94:e8:fa:8d:57:b5:
                    7d:cd:3b
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Alternative Name:
                DNS:mosquitto, DNS:cse, DNS:zigbee2mqtt, DNS:nodered, DNS:portainer, DNS:grafana
            X509v3 Subject Key Identifier:
                C9:8D:39:32:EA:7A:DD:86:BB:1F:B9:76:7A:3C:69:7B:BF:1C:C0:33
    Signature Algorithm: sha1WithRSAEncryption
         b1:e0:a1:b3:f5:91:3d:31:47:30:53:29:ef:8b:f1:81:8a:6c:
         c6:5c:90:a8:82:55:0e:88:ea:26:6b:2c:d2:1b:ff:4a:80:92:
         64:ae:20:41:ad:46:c5:ff:b0:24:f5:7c:aa:49:f5:12:ff:9e:
         23:bc:53:6e:0c:78:c1:91:1c:6c:30:71:34:b0:ac:b1:f9:0e:
         2c:b9:38:5d:1d:b7:d3:2e:63:3d:5f:83:c5:7b:69:ec:53:d9:
         4f:1b:50:ee:b8:61:1b:20:bf:86:00:24:c5:2b:0f:d3:e6:c3:
         d9:75:6f:86:4c:9e:22:e3:09:55:73:72:25:d8:c4:3e:36:31:
         e9:9b:d7:8d:c7:38:f4:9a:51:8a:d4:4f:d9:d1:6c:3e:44:99:
         3b:b0:f5:69:0d:32:16:c2:76:89:66:1e:4a:a2:94:a7:65:7c:
         93:58:bc:e1:57:93:1d:76:50:29:a7:ed:8c:8a:56:c8:a7:c3:
         d5:db:6c:8b:e5:59:43:0f:a9:f5:50:cc:50:f8:20:0a:a8:28:
         bd:92:61:54:b9:db:af:b2:0e:a8:48:3f:fd:25:c6:cc:4e:be:
         27:b6:ed:76:9e:99:ac:54:c9:68:4c:87:5a:51:9f:37:05:51:
         fd:54:c0:46:24:69:7a:9d:c6:db:59:d0:f9:b8:0a:c0:3b:d2:
         3a:14:d1:78:47:1d:a7:41:57:99:dd:93:bd:58:72:8c:ec:eb:
         6a:f9:d7:68:c2:37:6a:9a:8a:e3:ed:1c:d4:2e:7a:c9:08:0a:
         6a:62:5a:3d:e3:75:e5:9c:fe:c5:49:df:a2:86:3c:c1:04:20:
         58:37:17:7f:5e:a0:5e:7d:75:74:90:22:f0:06:3c:36:04:33:
         96:9f:b3:03:be:60:3e:f3:4e:ee:f5:22:fe:60:41:70:6e:ca:
         29:a7:a2:f0:d1:69:15:dd:49:d8:8c:2b:e0:5a:52:8b:b7:a4:
         45:d8:f4:90:a0:c7:08:d7:22:d3:e1:bc:65:43:da:c7:7f:49:
         81:1d:e6:bd:61:55:62:78:16:ff:1d:4a:c6:53:93:ad:04:b3:
         b2:40:84:15:2c:6d:a3:a8:94:51:bb:83:56:3d:ab:cf:18:7d:
         dc:45:2e:99:74:aa:d8:ca:36:e3:3c:20:ff:44:86:0b:91:87:
         a9:23:88:a0:42:43:1d:8a:fe:ef:18:e5:2b:62:71:3e:f9:0d:
         60:b0:39:c8:f3:13:9a:d6:47:64:97:f8:2a:96:4a:65:47:b5:
         cd:9f:9f:90:ef:b5:5c:7b:79:b8:49:b5:d9:77:fb:eb:60:2d:
         21:7c:8e:e5:b0:e1:87:d2:dc:2c:24:af:c5:01:0e:80:b0:51:
         87:44:be:b4:45:e4:f6:55
```

We can verify if the certificate is correct:
```
openssl verify -CAfile ca.crt mio_aid.crt
```

Output:
```
mio_aid.crt: OK
```

### Create private and public keys ###
```
openssl rsa -in server.key -text > private.pem
openssl x509 -inform PEM -in server.crt > public.pem
```

Credits to: https://gist.github.com/Soarez/9688998