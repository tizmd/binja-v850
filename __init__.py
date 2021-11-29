import binaryninja as bn

from .architecutre import V850Architecture, V850ESArchitecture, V850E2MArchitecture

V850Architecture.register()
V850ESArchitecture.register()
V850E2MArchitecture.register()

v850: bn.Architecture = bn.Architecture["v850"]
v850es: bn.Architecture = bn.Architecture["v850es"]
v850e2m: bn.Architecture = bn.Architecture["v850e2m"]

#bn.BinaryViewType["ELF"].register_arch(29925, bn.Endianness.LittleEndian, v850e2m)
#bn.BinaryViewType["ELF"].register_arch(29814, bn.Endianness.LittleEndian, v850es)
#bn.BinaryViewType["ELF"].register_arch(29646, bn.Endianness.LittleEndian, v850es)

bn.BinaryViewType["ELF"].register_arch(87, bn.Endianness.LittleEndian, v850)


class V850CallingConvention(bn.CallingConvention):
    int_arg_regs = ["r1"] + ["r%d" % i for i in range(5, 19)]
    int_return_reg = "r1"
    high_int_return_reg = "r5"
    callee_saved_regs = ["gp", "r25"]


v850.register_calling_convention(V850CallingConvention(v850, "default"))
v850es.register_calling_convention(V850CallingConvention(v850es, "default"))
v850e2m.register_calling_convention(V850CallingConvention(v850e2m, "default"))
