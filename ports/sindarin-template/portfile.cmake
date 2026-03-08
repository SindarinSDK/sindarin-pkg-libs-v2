vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO SindarinSDK/sindarin-template
    REF 2f7fe190b28f1d9c7e698ae95f1698d780dbc3fe
    SHA512 43d7815c2414d40dac78c9d0a60b4ccb744f6a3689c509533119d6d5f628c7e4081713ed18a92c3eb191f6afd2523dfe334b4eff2227c3892951cc4955961110
    HEAD_REF main
)

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}"
    OPTIONS
        -DBUILD_TESTING=OFF
)

vcpkg_cmake_install()
vcpkg_cmake_config_fixup(PACKAGE_NAME sindarin-template CONFIG_PATH lib/cmake/sindarin-template)

file(REMOVE_RECURSE "${CURRENT_PACKAGES_DIR}/debug/include")

file(WRITE "${CURRENT_PACKAGES_DIR}/share/${PORT}/copyright" "Copyright (c) SindarinSDK. All rights reserved.")
