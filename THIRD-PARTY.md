# Third-Party Licenses

This package bundles pre-built static libraries from the following open-source projects. Each library retains its original license.

## Permissive Licenses

### zlib
- **License:** zlib License (permissive)
- **Source:** https://zlib.net/
- **Copyright:** (C) 1995-2024 Jean-loup Gailly and Mark Adler

### yyjson
- **License:** MIT
- **Source:** https://github.com/ibireme/yyjson
- **Copyright:** Copyright (c) 2020 YaoYuan

### json-c
- **License:** MIT
- **Source:** https://github.com/json-c/json-c
- **Copyright:** Copyright (c) 2009-2012 Eric Haszlakiewicz
- **Copyright:** Copyright (c) 2004, 2005 Metaparadigm Pte Ltd

### libxml2
- **License:** MIT
- **Source:** https://gitlab.gnome.org/GNOME/libxml2
- **Copyright:** Copyright (C) 1998-2012 Daniel Veillard

### libyaml
- **License:** MIT
- **Source:** https://github.com/yaml/libyaml
- **Copyright:** Copyright (c) 2017-2020 Ingy dot Net
- **Copyright:** Copyright (c) 2006-2016 Kirill Simonov

### curl
- **License:** MIT/X derivative (curl License)
- **Source:** https://curl.se/
- **Copyright:** Copyright (c) 1996-2024 Daniel Stenberg

### http-parser
- **License:** MIT
- **Source:** https://github.com/nodejs/http-parser
- **Copyright:** Copyright Joyent, Inc. and other Node contributors

### ngtcp2
- **License:** MIT
- **Source:** https://github.com/ngtcp2/ngtcp2
- **Copyright:** Copyright (c) 2016 ngtcp2 contributors

### libssh2
- **License:** BSD 3-Clause
- **Source:** https://libssh2.org/
- **Copyright:** Copyright (c) 2004-2007 Sara Golemon
- **Copyright:** Copyright (c) 2005,2006 Mikhail Gusarov
- **Copyright:** Copyright (c) 2006-2007 The Written Word, Inc.
- **Copyright:** Copyright (c) 2007 Eli Fant
- **Copyright:** Copyright (c) 2009-2023 Daniel Stenberg

### pcre2
- **License:** BSD 3-Clause
- **Source:** https://github.com/PCRE2Project/pcre2
- **Copyright:** Copyright (c) 1997-2024 University of Cambridge

### utf8proc
- **License:** MIT
- **Source:** https://github.com/JuliaStrings/utf8proc
- **Copyright:** Copyright (c) 2014-2021 by Steven G. Johnson, Jiahao Chen, Peter Colberg, Tony Kelman, Scott P. Jones, and other contributors

### sindarin-template
- **License:** MIT
- **Source:** https://github.com/SindarinSDK/sindarin-template
- **Copyright:** Copyright (c) 2025-present CryoSharp

## Apache 2.0 Licensed

### OpenSSL
- **License:** Apache 2.0
- **Source:** https://www.openssl.org/
- **Copyright:** Copyright (c) 1998-2024 The OpenSSL Project Authors
- **Note:** OpenSSL 3.x is licensed under Apache 2.0. Earlier versions used a dual OpenSSL/SSLeay license.

### libmongoc / libbson
- **License:** Apache 2.0
- **Source:** https://github.com/mongodb/mongo-c-driver
- **Copyright:** Copyright (c) 2013-2024 MongoDB, Inc.

## Dual Licensed (BSD selected)

### Zstandard (zstd)
- **License:** BSD 3-Clause OR GPL 2.0 (BSD 3-Clause selected for this distribution)
- **Source:** https://github.com/facebook/zstd
- **Copyright:** Copyright (c) Meta Platforms, Inc. and affiliates

## Weak Copyleft (LGPL)

### libssh
- **License:** LGPL 2.1
- **Source:** https://www.libssh.org/
- **Copyright:** Copyright (c) 2003-2024 Aris Adamantiadis and contributors
- **Note:** This library is statically linked. Under LGPL 2.1 Section 6, users who wish to modify and relink this library may request the corresponding object files. The unmodified source code is available at the URL above.

### libmariadb (MariaDB Connector/C)
- **License:** LGPL 2.1 or later
- **Source:** https://github.com/mariadb-corporation/mariadb-connector-c
- **Copyright:** Copyright (c) 2012-2024 MariaDB Corporation Ab
- **Note:** This library is statically linked. Under LGPL 2.1 Section 6, users who wish to modify and relink this library may request the corresponding object files. The unmodified source code is available at the URL above. A commercial license is available from MariaDB Corporation.

## Copyleft with Linking Exception

### libgit2
- **License:** GPL 2.0 with Linking Exception
- **Source:** https://libgit2.org/
- **Copyright:** Copyright (C) the libgit2 contributors
- **Note:** The linking exception permits use in proprietary software without triggering GPL source disclosure requirements. The full exception text is included in the libgit2 source repository.

## PostgreSQL Licensed

### libpq / libpgcommon / libpgport / libpgtypes / libecpg
- **License:** PostgreSQL License (BSD-like, permissive)
- **Source:** https://www.postgresql.org/
- **Copyright:** Portions Copyright (c) 1996-2024 The PostgreSQL Global Development Group
- **Copyright:** Portions Copyright (c) 1994 The Regents of the University of California

## Public Domain

### SQLite
- **License:** Public Domain
- **Source:** https://www.sqlite.org/
- **Note:** SQLite is released into the public domain by its authors and has no license restrictions.

## System Libraries

The following system libraries are linked at build time but are not bundled:
- **glibc** (libm, libdl, libresolv, librt, libpthread) — LGPL 2.1, dynamically linked
- **Linux kernel headers** — GPL 2.0 with syscall exception

---

## License Compatibility Summary

All bundled libraries are compatible with the MIT license used by the Sindarin SDK. Users should be aware of the following obligations:

1. **LGPL libraries (libssh, libmariadb):** If you modify these libraries, you must make the modified source available. Static linking requires providing object files for relinking on request.
2. **Apache 2.0 libraries (OpenSSL, libmongoc):** Require preservation of copyright notices and a copy of the license in distributions.
3. **libgit2 (GPL 2.0 + linking exception):** The linking exception means no source disclosure is required for applications that link against it.
4. **All other libraries:** Require only preservation of copyright notices.
