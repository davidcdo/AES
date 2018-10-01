#Imports the Systems and Arrays
import sys
import array

# Key Arrays 
# Sub byte lookup table - Used by Sub_Bytes and Key Expansion
S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
    0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
    0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
    0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
    0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
    0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
    0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
    0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
    0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
    0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
    0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
    0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
    0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
    0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
    0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
    0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
    0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
    0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
    0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
    0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
    0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
    0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
    0x54, 0xbb, 0x16
]

# Inverted subByte lookup table
INV_S_BOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
    0x9e, 0x81, 0xf3, 0xd7, 0xfb, 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
    0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb, 0x54,
    0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
    0x42, 0xfa, 0xc3, 0x4e, 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
    0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25, 0x72, 0xf8,
    0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
    0x65, 0xb6, 0x92, 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
    0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84, 0x90, 0xd8, 0xab,
    0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
    0x45, 0x06, 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
    0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b, 0x3a, 0x91, 0x11, 0x41,
    0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
    0x73, 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
    0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e, 0x47, 0xf1, 0x1a, 0x71, 0x1d,
    0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
    0xfe, 0x78, 0xcd, 0x5a, 0xf4, 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
    0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f, 0x60,
    0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
    0x93, 0xc9, 0x9c, 0xef, 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
    0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61, 0x17, 0x2b,
    0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
    0x21, 0x0c, 0x7d
]

# AES Multiplication Lookup Tables
MUL2 = [
	0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
	0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e,
	0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e,
	0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e,
	0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e,
	0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe,
	0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde,
	0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe,
	0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05,
	0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25,
	0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45,
	0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65,
	0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85,
	0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5,
	0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5,
	0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5,
]

MUL3 = [
	0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11,
	0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21,
	0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71,
	0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41,
	0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1,
	0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1,
	0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1,
	0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81,
	0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a,
	0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba,
	0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea,
	0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda,
	0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a,
	0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a,
	0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a,
	0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a,
]

MUL9 = [
	0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77,
	0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7,
	0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c,
	0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc,
	0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01,
	0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91,
	0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a,
	0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa,
	0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b,
	0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b,
	0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0,
	0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30,
	0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed,
	0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d,
	0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6,
	0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46,
]

MUL11 = [
	0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69,
	0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9,
	0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12,
	0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2,
	0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f,
	0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f,
	0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4,
	0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54,
	0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e,
	0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e,
	0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5,
	0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55,
	0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68,
	0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8,
	0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13,
	0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3,
]

MUL13 = [
	0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b,
	0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b,
	0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0,
	0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20,
	0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26,
	0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6,
	0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d,
	0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d,
	0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91,
	0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41,
	0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a,
	0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa,
	0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc,
	0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c,
	0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47,
	0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97,
]

MUL14 = [
	0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a,
	0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba,
	0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81,
	0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61,
	0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7,
	0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17,
	0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c,
	0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc,
	0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b,
	0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb,
	0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0,
	0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20,
	0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6,
	0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56,
	0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d,
	0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d,
]

# Congruence LookUp Table used in the function get_key_expansion
R_CON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]

# Define and initializes constants
# Initializes arguments from sys.argv
keysize = None
keyfile = None
inputfile = None
outputfile = None
mode = None

# Initializes key values used by AES
num_keys = -1
num_rounds = -1

# Sets the values from the args to the initializes constants
def setArgs():
	args = getArgs(sys.argv)

	global keysize, keyfile, inputfile, outputfile, mode

	keysize = int(args['--keysize'])
	keyfile = args['--keyfile']
	inputfile = args['--inputfile']
	outputfile = args['--outputfile']
	mode = args['--mode']

	checkArgs()

# Parse the arguments from sys.argv
def getArgs(argv):
	list_args = {}
	while argv:
		if argv[0][0] == '-' and argv[0][1] == '-':
			list_args[argv[0]] = argv[1]
		argv = argv[1:]
	return list_args

# Helper method to setArgs that checks for correct arguments
def checkArgs():
	if (keysize != 128 and keysize != 256):
		print("ERROR: Please enter the correct keysize <128 or 256>")
		sys.exit()
	elif (keyfile == None or inputfile == None or outputfile == None):
		if (keyfile == None):
			print("ERROR: Missing keyfile")
		if (inputfile == None):
			print("ERROR: Missing inputfile")
		if (outputfile == None):
			print("ERROR: Missing outputfile")
		sys.exit()
	elif (mode != "encrypt" and mode != "decrypt"):
		print("ERROR: Please enter a correct mode <encrypt or decrypt>")
		sys.exit()

#
def get_key_expansion(key_file_bytes):
	global num_keys, num_rounds

	# Checks and Computes the correct number of keys and number of rounds
	if keysize == 128:
		num_keys = 4
		num_rounds = 10
	elif keysize == 256:
		num_keys = 8
		num_rounds = 14

	if (num_keys == -1 or num_rounds == -1):
		print("ERROR: Unable to compute the number",  
			"of words in a cipher key or number of rounds", 
			"using the current keyfile")
		sys.exit()

	"""
	References the Pseudo Code under FIPS 197, Advanced Encryption Standard (AES)
	
	KeyExpansion(byte key[4*Nk], word w[Nb*(Nr+1)], Nk)
	begin
		word temp
		i = 0

		while (i < Nk)
			w[i] = word(key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
			i = i+1
		end while

		i = Nk

		while (i < Nb * (Nr+1)]
			temp = w[i-1]
			if (i mod Nk = 0)
				temp = SubWord(RotWord(temp)) xor Rcon[i/Nk]
			else if (Nk > 6 and i mod Nk = 4)
				temp = SubWord(temp)
			end if
			w[i] = w[i-Nk] xor temp
			i = i + 1
		end while
	end
	"""
	# Initializes the array of keys 
	key_expansion = []

	# Needs to take the first num_keys of keys and expand it
	for i in range (0, num_keys):
		"""
		print("Hey! Expanding first num_keys")
		print(num_keys)
		print(num_rounds)
		"""
		key_expansion += ([key_file_bytes[4 * i]] + 
			[key_file_bytes[4 * i + 1]] + 
			[key_file_bytes[4 * i + 2]] + 
			[key_file_bytes[4 * i + 3]])

	# Needs to expand the remaining bytes left within the key
	for i in range(num_keys, 4 * (num_rounds + 1)):
		"""
		print("Hey! Expanding remaining num_keys")
		print(num_keys)
		print(num_rounds)
		"""
		temp = key_expansion[4 * (i - 1) : 4 * i]
		
		if i % num_keys == 0:
			# Shifts the (Column - 1)th column
			# Shift e.g. a0, a1, a2, a3 to a1, a2, a3, a0
			# SubBytes the whole row by its corresponding S_BOX
			temp = temp[1 : 4] + [temp[0]]
			for a in range (0, 4):
				temp[a] = S_BOX[temp[a]]

			# Gets corresponding Congruence value
			con = R_CON[i // num_keys - 1]

			# XOR the first column with 'con'
			# Remaining 3 columns will be XOR with 0
			temp[0] = temp[0] ^ con
			for a in range (1, 4): 
				temp[a] = temp[a] ^ 0
		elif (i % num_keys == 4) and (num_keys == 8):
			# Simply just SubByte the entire column with its corresponding S_BOX
			for a in range (0, 4):
				temp[a] = S_BOX[temp[a]]

		key_expansion += ([key_expansion[4 * (i - num_keys)] ^ temp[0]] +  
			[key_expansion[4 * (i - num_keys) + 1] ^ temp[1]] + 
			[key_expansion[4 * (i - num_keys) + 2] ^ temp[2]] + 
			[key_expansion[4 * (i - num_keys) + 3] ^ temp[3]])


	return key_expansion

# Helper method to determine whether to encrypt or decrypt
def get_output(key_expansion, input_file_bytes):
	if mode == 'encrypt':
		print("I'm encrypting")
		return encrypt(key_expansion, input_file_bytes)
	elif mode == 'decrypt':
		print("I'm decrypting")
		return decrypt(key_expansion, input_file_bytes)
	else:
		print("ERROR: Cannot compute outputfile,",
			"mode does not equal encrypt or decrypt")
		sys.exit()

# Encrypts the inputfile
def encrypt(key_expansion, input_file_bytes):
	# Initializes key values
	output = []
	file_len = len(input_file_bytes)

	# Add necessary paddings 
	# Uses ZeroLength paddings
	# Gets remaining pad needed and extends input_bytes_file
	zero_paddings = 16 - (file_len % 16)
	input_file_bytes.extend([0] * zero_paddings)
	input_file_bytes[-1] = zero_paddings

	# New file_len
	file_len = len(input_file_bytes)

	# Starts encryption by blocks coming from the inputfile
	for i in range (0, file_len, 16):
		# Encrypts the block of 16 bytes, only 16 blocks at a time
		currentBlock = input_file_bytes[i : (i + 16)]

		# Initializes the state and add the initial 'AddRoundKey' to it
		# This is initialize with 'currentBlock'
		state = [[0 for _ in range(0, 4)] for _ in range(0, 4)]

		pos = 0

		# First 16 bytes will be arranged in column order, 
		# not by the original row order
		for a in range (0, 4):
			for b in range (0, 4):
				state[b][a] = currentBlock[pos]
				pos += 1

		# Finally initializes the first roundKey
		state = addRoundKey(state, key_expansion, 0)

		# Uses AES standard procedure, cycle of rounds - Normal Rounds
		# Procedure cycle order - subBytes, shiftRows, mixColumns, addRoundKey
		for rounds in range(1, num_rounds):
			state = subBytes(state)
			state = shiftRows(state)
			state = mixColumns(state)
			state = addRoundKey(state, key_expansion, rounds * 16)

		# Uses AES standard procedure, Final Round
		# subBytes, shiftRows, and addRoundKey (excludes mixColumns)
		state = subBytes(state)
		state = shiftRows(state)
		state = addRoundKey(state, key_expansion, num_rounds * 16)

		# Reorganizes again for Column order
		for a in range(0, 4):
			for b in range(0, 4):
				output.append(state[b][a])

	return output

# Decrypts the inputfile
def decrypt(key_expansion, input_file_bytes):
	# Initializes key values
	output = []
	file_len = len(input_file_bytes)

	# Starts decryption by blocks coming from the inputfile
	for i in range (0, file_len, 16):
		# Decrypts the block of 16 bytes, only 16 blocks at a time
		currentBlock = input_file_bytes[i : (i + 16)]

		# Initializes the state and add the initial 'AddRoundKey' to it
		# This is initialize with 'currentBlock'
		state = [[0 for _ in range(0, 4)] for _ in range(0, 4)]

		pos = 0

		# First 16 bytes will be arranged in column order, 
		# not by the original row order
		for a in range (0, 4):
			for b in range (0, 4):
				state[b][a] = currentBlock[pos]
				pos += 1

		"""
		Decryption of rounds is inverse of the encryption of rounds
		Operations are inverse - starts at the back of the RoundKeys
		Thus, addRoundKey must start at num_rounds * 16, 
		then rounds * 16, then finally 0 (initial roundkey)
		"""

		# Finally initializes the first roundKey
		state = addRoundKey(state, key_expansion, num_rounds * 16)

		# Normal Rounds
		# Uses AES standard procedure, cycle of rounds - Normal Rounds
		# Procedure cycle order - subBytes, shiftRows, mixColumns, addRoundKey
		for rounds in range(1, num_rounds):
			state = invSubBytes(state)
			state = invShiftRows(state)
			state = invMixColumns(state)
			state = addRoundKey(state, key_expansion, rounds * 16)

		# Final Rounds 
		# Uses AES standard procedure, Final Round
		# subBytes, shiftRows, and addRoundKey (excludes mixColumns)
		state = invSubBytes(state)
		state = invShiftRows(state)
		state = addRoundKey(state, key_expansion, 0)


		# Reorganizes again for Column order
		for a in range(0, 4):
			for b in range(0, 4):
				output.append(state[b][a])

	return output

# Add Round Key Transformation
def addRoundKey(state, key_expansion, num):
	pos = int(num)

	"""
	Followings the following transformatioin ...
		[s'0c,s'1c,s'2c,s'3c] = [s0c,s1c,s2c,s3c] ^ [w(round)*Nb + c]

	It is a transformation that combines the RoundKey (key_expansion)
	with the current state via XOR

	This function will be used during the initial round and the cycle 
	of rounds of encryption and decryption

	"""
	"""
	for c in range(0, 4):
		temp0 = state[0][c] ^ key_expansion[pos + c]
		temp1 = state[1][c] ^ key_expansion[pos + c]
		temp2 = state[2][c] ^ key_expansion[pos + c]
		temp3 = state[3][c] ^ key_expansion[pos + c]

		state[0][c] = temp0
		state[1][c] = temp1
		state[2][c] = temp2
		state[3][c] = temp3

	"""
	for i in range(0, 4):
		for j in range(0, 4):
			state[j][i] = state[j][i] ^ key_expansion[pos]
			pos += 1

	return state

# Sub-byte Transformation 
def subBytes(state):
	"""
	Iterates through the State in a manner that matches the S_BOX's
	16 by 16 grid, 256 bytes (Hence the range up to 4). As it is 
	iterating through the State, it replaces the current byte with
	another byte from the S_BOX
	"""
	for i in range(0, 4):
		for j in range (0, 4):
			state[i][j] = S_BOX[state[i][j]]
	return state

# Shift-row Transformation
def shiftRows(state):
	"""
	Shifts the row to the left in accordance to the current row
	First Row, does not shift
	Second Row, shifts once to the left
	Third Row, shifts twice to the left
	Fourth Row, shifts thice to the left
	Any byte that 'falls off' will reappear to the right of the same row
	"""

	# Creates a temporary array to store an already 'shifted' row
	temp = [0 for _ in range(0, 4)]
	# Ignores the first row, covers second, third, and fourth row
	for i in range (1, 4):
		for j in range (0, 4):
			"""
			Stores shifted row depending on the current row
			Ex - Row 2 will start storing at index 1 ...
			Ex - Row 3 will start storing at index 2 ...
			Ex - Row 4 will start storing at index 3 ...
			"""
			temp[j] = state[i][(i + j) % 4]
		for j in range (0, 4):
			# Takes the temporary shifted row and apply it to the actual state
			state[i][j] = temp[j]

	return state

# Mix Column Transformation
def mixColumns(state):
	""" 
	During the encryption process of mix-column transformation, it requires
	the multiplication of every column of the current state with a fixed
	polinomial of a(x) = {03}x^3 + {01}x^2 + {01}x + {02} . 
	
	This results in a matrix of ...
			02 03 01 01
			01 02 03 01
			01 01 02 03 
			03 01 01 02

	In a setting where i determines the row and j determines the column
	01 simply means a state of state[i][j]
	02 uses MUL2 with the addition of the state[i][j] resulting MUL2[state[i][j]]
	02 uses MUL3 with the addition of the state[i][j] resulting MUL3[state[i][j]]

	In the end, computation operates column by column, XOR'ing the entire 
	column with the adjusted matrix for a single new byte.
	"""
	for i in range (0, 4):
		# Executes the mix-colum transformation
		temp0 = MUL2[state[0][i]] ^ MUL3[state[1][i]] ^ state[2][i] ^ state[3][i]
		temp1 = state[0][i] ^ MUL2[state[1][i]] ^ MUL3[state[2][i]] ^ state[3][i]
		temp2 = state[0][i] ^ state[1][i] ^ MUL2[state[2][i]] ^ MUL3[state[3][i]]
		temp3 = MUL3[state[0][i]] ^ state[1][i] ^ state[2][i] ^ MUL2[state[3][i]]

		# Correctly copies into the state 
		state[0][i] = temp0 
		state[1][i] = temp1
		state[2][i] = temp2
		state[3][i] = temp3

	return state

# Inverted subByte transformation
def invSubBytes(state):
	# Implemented in the opposite way of subByte -- uses INV_S_BOX instead
	for i in range (0, 4):
		for j in range (0, 4):
			state[i][j] = INV_S_BOX[state[i][j]]
	return state

# Inverted ShiftRow Transformation
def invShiftRows(state):
	# Implemented in the opposite way of shiftRow 
	# Instead of temp[j] = state[i][(i + j) % 4]
	# It is now temp[(i + j) % 4] = state[i][j]
	temp = [0 for _ in range(0, 4)]
	for i in range(1, 4):
		for j in range(0, 4):
			temp[(i + j) % 4] = state[i][j]
		for j in range(0, 4):
			state[i][j] = temp[j]
	return state

# Inverted MixColumns Transformation
def invMixColumns(state):
	#Very similar to MixColumns Transformation
	"""
	Applies the inverse of a(x) = {03}x^3 + {01}x^2 + {01}x + {02}
	From the FIPS pdf file, a^-1(x) = {0b}x^3 + {0d}x^2 + {09}x + {0e}

	In matrix form... it becomes ...

			0e 0b 0d 09
			09 0e 0b 0d
			0d 09 0e 0b
			0b 0d 09 0e

	Converted to decimal values (from hexidecimal) ...
	0e is MUL14, 0b is MUL11, 0d is MUL13, and 09 is of course, MUL9
	"""
	for i in range (0, 4):
		# Executes the inverted mix-colum transformation
		temp0 = MUL14[state[0][i]] ^ MUL11[state[1][i]] ^ MUL13[state[2][i]] ^ MUL9[state[3][i]]
		temp1 = MUL9[state[0][i]] ^ MUL14[state[1][i]] ^ MUL11[state[2][i]] ^ MUL13[state[3][i]]
		temp2 = MUL13[state[0][i]] ^ MUL9[state[1][i]] ^ MUL14[state[2][i]] ^ MUL11[state[3][i]]
		temp3 = MUL11[state[0][i]] ^ MUL13[state[1][i]] ^ MUL9[state[2][i]] ^ MUL14[state[3][i]]

		# Correctly copies into the state 
		state[0][i] = temp0 
		state[1][i] = temp1
		state[2][i] = temp2
		state[3][i] = temp3

	return state

# Main function, starts everything up
def main():
	setArgs()

	# Opens and reads the files sent in from argv
	# "rb" means to read the file in binary
	# "wb" means to write the file in binary
	key_file = open(keyfile, 'rb')
	input_file = open(inputfile, 'rb')
	output_file = open(outputfile, 'wb')

	#print("Content of key_file", key_file.read())
	#print("Content of input_file", input_file.read())
	#print("Content of output_file", output_file.read())

	# The following function uses 'bytearray' returns an array of bytes 
	# thats reads from key_file or input_file into the 
	# following variables: key_file_bytes and input_file_bytes
	key_file_bytes = bytearray(key_file.read())
	input_file_bytes = bytearray(input_file.read())

	# Computes the key expansion from the key_file_bytes
	key_expansion = get_key_expansion(key_file_bytes)

	# Encrypts or Decrypts
	outputdata = get_output(key_expansion, input_file_bytes)


	# Writes to the output_file
	# Converts the output into a format that's user friendly and then writes
	#outputdata = array.array('B', outputdata)
	outputdata = bytearray(outputdata)
	output_file.write(outputdata)

	# Closes the files
	key_file.close()
	input_file.close()
	output_file.close()

if __name__ == "__main__":
	main()
