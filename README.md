# Sindarin Libs

Pre-built static libraries for Sindarin projects. Libraries are built via GitHub Actions and distributed as release assets.

## Quick Install

**Linux/macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/SindarinSDK/sindarin-pkg-libs-v2/main/scripts/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/SindarinSDK/sindarin-pkg-libs-v2/main/scripts/install.ps1 | iex
```

These commands download and extract the latest libraries to `./libs` in your current directory.

## Supported Platforms

- **Linux** (x64-linux)
- **macOS** (x64-osx / arm64-osx)
- **Windows** (x64-mingw-static)

## Included Libraries

| Library | Description |
|---------|-------------|
| zlib | Compression library |
| yyjson | High-performance JSON parser |
| libxml2 | XML parsing library |
| libyaml | YAML parsing library |
| OpenSSL | SSL/TLS cryptography |
| ngtcp2 | QUIC protocol implementation |
| libssh | SSH library |
| libgit2 | Git implementation |
| curl | HTTP client library |

## Extracted Directory Structure

After installation, the `libs` directory contains:

```
libs/
├── lib/          # Static libraries (.a files)
├── include/      # Header files
└── share/        # CMake config files
```

## Usage in CMake

```cmake
# Set paths (adjust based on your project structure)
set(SINDARIN_LIBS_DIR "${CMAKE_SOURCE_DIR}/libs")
set(SINDARIN_LIBS_INCLUDE "${SINDARIN_LIBS_DIR}/include")
set(SINDARIN_LIBS_LIB "${SINDARIN_LIBS_DIR}/lib")

# Add include path
include_directories(${SINDARIN_LIBS_INCLUDE})

# Link libraries
target_link_libraries(your_target
    "${SINDARIN_LIBS_LIB}/libcurl.a"
    "${SINDARIN_LIBS_LIB}/libgit2.a"
    "${SINDARIN_LIBS_LIB}/libssh.a"
    "${SINDARIN_LIBS_LIB}/libssl.a"
    "${SINDARIN_LIBS_LIB}/libcrypto.a"
    "${SINDARIN_LIBS_LIB}/libz.a"
    # ... other libraries as needed
)
```

## Building Locally

### Prerequisites

- CMake 3.20+
- Ninja
- Git
- Python 3
- Platform-specific:
  - **Linux**: GCC, build-essential
  - **macOS**: Xcode Command Line Tools
  - **Windows**: LLVM-MinGW

### Build Commands

```bash
# Setup vcpkg and install dependencies
make setup

# Build libraries to libs/{platform}/
make build

# Clean build artifacts
make clean

# Full rebuild
make rebuild

# Show configuration
make info
```

## GitHub Actions

The workflow builds libraries on all three platforms and uploads them as release assets.

### Creating a Release

1. Create a new release on GitHub with a version tag (e.g., `v1.0.0`)
2. The workflow automatically builds all platforms and attaches the archives to the release

Alternatively, trigger manually via the Actions UI with a tag name.

## Updating Dependencies

1. Edit `vcpkg.json` to add/modify dependencies
2. Create a new release to trigger builds
3. Archives will be attached to the release

## License

The build system is provided as-is. Individual libraries retain their original licenses:
- zlib: zlib license
- yyjson: MIT
- libxml2: MIT
- libyaml: MIT
- OpenSSL: Apache 2.0
- ngtcp2: MIT
- libssh: LGPL 2.1
- libgit2: GPL 2.0 with linking exception
- curl: MIT/X derivate
