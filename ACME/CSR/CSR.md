## Generate Keys and Certificate Signing Request (CSR) ##

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

Output:
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
ERROR:There is already a certificate for /C=AT/ST=Vienna/O=MIO_AID/CN=localhost
The matching entry has the following details
Type          :Valid
Expires on    :231106202122Z
Serial Number :01
File name     :unknown
Subject Name  :/C=AT/ST=Vienna/O=MIO_AID/CN=localhost
```

Now we have a certificate that includes SubjectAltNames:
```
openssl ca -config ca.conf -out mio_aid.crt -extfile mio_aid.extensions.conf -in mio_aid.csr

```