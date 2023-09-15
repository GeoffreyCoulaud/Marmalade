from enum import Enum


class Architecture(str, Enum):
    ARM = "Arm"
    ARM64 = "Arm64"
    S390X = "S390x"
    WASM = "Wasm"
    X64 = "X64"
    X86 = "X86"

    def __str__(self) -> str:
        return str(self.value)
