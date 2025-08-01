#!/usr/bin/env python3
import json

# toolchain, url
toolchain_list = [
    "aarch64-gcc",
    "arm-clang",
    "arm-iar",
    "arm-gcc",
    "esp-idf",
    "msp430-gcc",
    "riscv-gcc",
    "rx-gcc"
]

# family: [supported toolchain]
family_list = {
    "at32f402_405 at32f403a_407 at32f413 at32f415 at32f423 at32f425 at32f435_437": ["arm-gcc"],
    "broadcom_32bit": ["arm-gcc"],
    "broadcom_64bit": ["aarch64-gcc"],
    "ch32v10x ch32v20x ch32v30x fomu gd32vf103": ["riscv-gcc"],
    "da1469x": ["arm-gcc"],
    "imxrt": ["arm-gcc", "arm-clang"],
    "kinetis_k kinetis_kl kinetis_k32l2": ["arm-gcc", "arm-clang"],
    "lpc11 lpc13 lpc15": ["arm-gcc", "arm-clang"],
    "lpc17 lpc18 lpc40 lpc43": ["arm-gcc", "arm-clang"],
    "lpc51 lpc54 lpc55": ["arm-gcc", "arm-clang"],
    "maxim": ["arm-gcc"],
    "mcx": ["arm-gcc"],
    "mm32": ["arm-gcc"],
    "msp430": ["msp430-gcc"],
    "msp432e4 tm4c": ["arm-gcc"],
    "nrf": ["arm-gcc", "arm-clang"],
    "ra": ["arm-gcc"],
    "rp2040": ["arm-gcc"],
    "rx": ["rx-gcc"],
    "samd11 saml2x": ["arm-gcc", "arm-clang"],
    "samd21": ["arm-gcc", "arm-clang"],
    "samd5x_e5x samg": ["arm-gcc", "arm-clang"],
    "stm32c0 stm32f0 stm32f1 stm32f2 stm32f3": ["arm-gcc", "arm-clang", "arm-iar"],
    "stm32f4": ["arm-gcc", "arm-clang", "arm-iar"],
    "stm32f7": ["arm-gcc", "arm-clang", "arm-iar"],
    "stm32g0 stm32g4 stm32h5": ["arm-gcc", "arm-clang", "arm-iar"],
    "stm32h7 stm32h7rs": ["arm-gcc", "arm-clang", "arm-iar"],
    "stm32l0 stm32l4": ["arm-gcc", "arm-clang", "arm-iar"],
    "stm32n6": ["arm-gcc"],
    "stm32u5 stm32wb": ["arm-gcc", "arm-clang", "arm-iar"],
    "xmc4000": ["arm-gcc"],
    "-bespressif_s2_devkitc": ["esp-idf"],
    # S3, P4 will be built by hil test
    # "-bespressif_s3_devkitm": ["esp-idf"],
    # "-bespressif_p4_function_ev": ["esp-idf"],
}


def set_matrix_json():
    matrix = {}
    for toolchain in toolchain_list:
        filtered_families = [family for family, supported_toolchain in family_list.items() if
                             toolchain in supported_toolchain]
        matrix[toolchain] = filtered_families

    print(json.dumps(matrix))


if __name__ == '__main__':
    set_matrix_json()
