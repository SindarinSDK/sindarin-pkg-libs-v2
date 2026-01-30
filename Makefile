# Sindarin Libs Makefile
# Cross-platform wrapper for CMake build system

# Detect platform
ifeq ($(OS),Windows_NT)
    PLATFORM := windows
    CMAKE_PRESET := ci-windows
    TRIPLET := x64-mingw-static
    PYTHON := python
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Darwin)
        PLATFORM := macos
        UNAME_M := $(shell uname -m)
        ifeq ($(UNAME_M),arm64)
            CMAKE_PRESET := ci-macos-arm64
            TRIPLET := arm64-osx
        else
            CMAKE_PRESET := ci-macos
            TRIPLET := x64-osx
        endif
    else
        PLATFORM := linux
        CMAKE_PRESET := ci-linux
        TRIPLET := x64-linux
    endif
    PYTHON := python3
endif

# Allow preset override
ifdef PRESET
    CMAKE_PRESET := $(PRESET)
endif

# Directories
BUILD_DIR := build/$(CMAKE_PRESET)
LIBS_DIR := libs/$(PLATFORM)
VCPKG_DIR := vcpkg
VCPKG_INSTALLED := vcpkg_installed/$(TRIPLET)

.PHONY: all setup build clean rebuild info help

# Default target
all: build

# Display help
help:
	@echo "Sindarin Libs Build System"
	@echo ""
	@echo "Targets:"
	@echo "  setup    - Install vcpkg and dependencies"
	@echo "  build    - Build and copy libraries to libs/$(PLATFORM)"
	@echo "  rebuild  - Clean and rebuild"
	@echo "  clean    - Remove build artifacts"
	@echo "  info     - Display build configuration"
	@echo ""
	@echo "Current configuration:"
	@echo "  Platform: $(PLATFORM)"
	@echo "  Preset:   $(CMAKE_PRESET)"
	@echo "  Triplet:  $(TRIPLET)"
	@echo ""
	@echo "Override preset with: make PRESET=<preset> <target>"

# Display build info
info:
	@echo "Platform:      $(PLATFORM)"
	@echo "CMake Preset:  $(CMAKE_PRESET)"
	@echo "Triplet:       $(TRIPLET)"
	@echo "Build Dir:     $(BUILD_DIR)"
	@echo "Libs Dir:      $(LIBS_DIR)"
	@echo "Vcpkg Dir:     $(VCPKG_DIR)"

# Setup vcpkg and install dependencies
setup:
	@echo "Setting up dependencies for $(PLATFORM)..."
	$(PYTHON) scripts/setup_deps.py --triplet=$(TRIPLET)

# Build libraries
build: $(VCPKG_INSTALLED)
	@echo "Building libraries for $(PLATFORM)..."
	cmake --preset $(CMAKE_PRESET) \
		-DVCPKG_TARGET_TRIPLET=$(TRIPLET) \
		-DVCPKG_INSTALLED_DIR=$(CURDIR)/vcpkg_installed
	cmake --build --preset $(CMAKE_PRESET)
	@echo ""
	@echo "Libraries built to: $(LIBS_DIR)"

# Ensure vcpkg dependencies are installed
$(VCPKG_INSTALLED):
	@echo "Dependencies not found. Running setup..."
	$(MAKE) setup

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build
	rm -rf libs/$(PLATFORM)
	@echo "Clean complete."

# Clean everything including vcpkg
clean-all: clean
	@echo "Cleaning vcpkg..."
	rm -rf vcpkg
	rm -rf vcpkg_installed
	@echo "Full clean complete."

# Rebuild from scratch
rebuild: clean build

# Verify build output
verify:
	@echo "Verifying build output..."
	@if [ -d "$(LIBS_DIR)/lib" ]; then \
		echo "Library directory: $(LIBS_DIR)/lib"; \
		ls -la $(LIBS_DIR)/lib/*.a 2>/dev/null || echo "No .a files found"; \
	else \
		echo "Error: $(LIBS_DIR)/lib does not exist"; \
		exit 1; \
	fi
	@if [ -d "$(LIBS_DIR)/include" ]; then \
		echo "Include directory: $(LIBS_DIR)/include"; \
		ls $(LIBS_DIR)/include | head -10; \
	else \
		echo "Error: $(LIBS_DIR)/include does not exist"; \
		exit 1; \
	fi
	@echo "Verification complete."
