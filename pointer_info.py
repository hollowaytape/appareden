"""
  Info for Appareden pointers to reassign or specify.
  Pointer table locations not included here, since that is info about rom structure.
"""

POINTER_DISAMBIGUATION = {
    # ORFIELD
    0x3fe8: 0x1ffc,
    0x26858: 0x1313f,
    0x2896c: 0x1d93d,
    0x2ea5d: 0x23190,
    0x2ea44: 0x2314b,
    0x2ea2b: 0x230e6,
    0x28f66: 0x1fc48,
    0x28385: 0x1b228,
    0x263be: 0xbe10,
    0x263cf: 0xbe2c,
    0x26e9d: 0x167d6,
    0x26ef9: 0x16e07,
    0x2718d: 0x16abf,
    0x271a2: 0x16bbc,
    0x271aa: 0x16bf2,
    0x271c1: 0x16e80,
    0x2900e: 0x204af,
    0x2e9e2: 0x22f68,
    0x26b64: 0x15e3e,
    0x290a1: 0x20d10,
    0x2eb50: 0x2324d,
    0x2e9b2: 0x22e57,
    0x2eab3: 0x2346b,
    0x28355: 0x1b14a,
    0x28c78: 0x1f191,    # Is this colliding with an ORBTL one? Let's see...(apparently not)
    0x28f90: 0x1fce4,
    0x2d111: 0x21720,
    0x2d24d: 0x21edc,
    0x2d298: 0x220d7,
    0x2d30c: 0x2239a,
    0x2d3a9: 0x2d396,   # Ocean Dragon Pill -> Unable to use that here
    0x27546: 0x177d9,
    0x2ea1c: 0x23099,   # Fixes the wait bug
    0x2ea20: 0x23064,
    0x2ea14: 0x2308a,   # Spirit2 HP pointer bug
    0x2ea1f: 0x230c0,   # Spirit2 HP pointer bug, part 2
    0x271b3: 0x16d60,

      # ORBTL
      0x27359: 0x13bfd,
      0x25376: 0xd277,
      0x2538f: 0xd422,
      0x2539c: 0xd53d,
      0x253a7: 0xd658,
      0x25330: 0xcf33,
      0x25349: 0xcf56,
      0x25359: 0xcfa6,
}

POINTERS_TO_REASSIGN = {
    'ORFIELD.EXE': [
            (0x2dc17, 0x2dbf4),   # Blaze2, Blaze3 descriptions
            (0x2dc3a, 0x2dbf4),
            (0x2dc80, 0x2dc5d),
            (0x2dca3, 0x2dc5d),
            (0x2dce9, 0x2dcc6),
            (0x2dd2f, 0x2dd0c),
            (0x2dd52, 0x2dd0c),
            (0x2dd98, 0x2dd75),
            (0x2ddbb, 0x2dd75),
            (0x2de01, 0x2ddde),
            (0x2de47, 0x2de24),
            (0x2de6a, 0x2de24),
            (0x2deb0, 0x2de8d),
            (0x2df19, 0x2def6),
            (0x2df3c, 0x2def6),
            (0x2df82, 0x2df5f),
            (0x2dfa5, 0x2df5f),
            (0x2dfeb, 0x2dfc8),
            (0x2e031, 0x2e00e),
            (0x2e054, 0x2e00e),
            (0x2e09a, 0x2e077),
            (0x2e0bd, 0x2e077),
            (0x2e103, 0x2e0e0),
            (0x28315, 0x2826a),
            (0x2826f, 0x2831b),
            (0x28272, 0x28320),
            (0x28277, 0x28326),
            (0x28c66, 0x2826a),
            (0x28c6c, 0x2831b),
            (0x28c72, 0x28320),
            (0x28c78, 0x28326),
            (0x28fcf, 0x2826a),
            (0x28fd5, 0x2831b),
            (0x28fdb, 0x28320),
            (0x28fe1, 0x28326),
            (0x2908b, 0x2826a),
            (0x290a5, 0x2826a),
            (0x290ab, 0x2831b),
            (0x290b1, 0x28320),
            (0x290b7, 0x28326),
            (0x2d056, 0x2e9b2),
            (0x2d06f, 0x2e9cb),
            (0x2d07a, 0x2e9d6),
            (0x2d097, 0x2e9b2),
            (0x2d0b0, 0x2e9cb),
            (0x2d0bb, 0x2e9d6),
            (0x2d0c7, 0x2d086),
            (0x2d0d8, 0x2e9b2),

            (0x2d100, 0x2d086),
            (0x2d111, 0x2e9b2),
            (0x2d12a, 0x2e9cb),
            (0x2d135, 0x2e9d6),
            (0x2d141, 0x2d086),
            (0x2d152, 0x2e9b2),
            (0x2d16b, 0x2e9cb),
            (0x2d176, 0x2e9d6),
            (0x2d182, 0x2d086),
            (0x2d193, 0x2e9b2),
            (0x2d1e9, 0x2826a),
            (0x2d219, 0x2826a),
            (0x2d247, 0x2826a),
            (0x2d27b, 0x2826a),

            (0x2e9fb, 0x2e9b2),
            (0x2ea14, 0x2e9cb),
            (0x2ea1f, 0x2e9d6),
            (0x2ea2b, 0x2e9e2),
            (0x2ea44, 0x2e9b2),
            (0x2ea5d, 0x2d0f1),
            (0x2ea6c, 0x2e9e2),
            (0x2eca7, 0x2eb6e),
            (0x2eb7c, 0x2e9d6),
            (0x2eba5, 0x2e9e2),
            (0x2ec89, 0x2eb50),
            (0x2ecb5, 0x2e9d6),
            (0x2ecc3, 0x2eb8a),
            (0x2ecde, 0x2e9e2),
            (0x2edc2, 0x2eb50),
            (0x2edf8, 0x2eb8a),
            (0x2ee13, 0x2e9e2),
            (0x2ee5c, 0x2e9e2),
            (0x2ee8a, 0x2e9e2),
            (0x2eea9, 0x2d264),
            (0x2eec0, 0x2e9e2),
            (0x2eed9, 0x2d396),

            (0x2d21f, 0x2d1ef),  # "Unable to use"
            (0x2d24d, 0x2d1ef),
            (0x2d281, 0x2d1ef),
            (0x2d2b2, 0x2d1ef),
            (0x2d2e5, 0x2d1ef),
            (0x2d316, 0x2d1ef),
            (0x2d347, 0x2d1ef),
            (0x2d378, 0x2d1ef),

            #(0x2d2db, 0x2d2a8),   # "points"
            #(0x2d30c, 0x2d2a8),
            #(0x2d33d, 0x2d2a8),
            #(0x2d36e, 0x2d2a8),

            (0x26883, 0x2ee32),     # &f came back to life
            (0x2d1da, 0x2ee32),
            (0x2ee7b, 0x2ee32),

            (0x27549, 0x26eec),      # &f purchased

            (0x2692c, 0x266a3),      # What will you do?
            (0x28044, 0x266a3), 

            (0x2e5f1, 0x2e506),      # Holy Light
            (0x2e600, 0x2e515),      # Santa Lucia
            (0x2e60d, 0x2e522),      # Hallelujah

            (0x26ec9, 0x26b64),      # &5Not enough gold.
            (0x27531, 0x26b64),

            (0x271c1, 0x26e9d),      # Are you sure?
            (0x27507, 0x26e9d),

            (0x2666a, 0x26641),     # &f acquired

            (0x26679, 0x26650),      # &5inventory is full

            (0x26690, 0x26667),      # &5
            (0x26855, 0x26667),
            (0x26880, 0x26667),
            (0x26892, 0x26667),
            (0x268c8, 0x26667),
            (0x268e0, 0x26667),
            (0x26ede, 0x26667),
            (0x26ee6, 0x26667),
            (0x27546, 0x26667),
            (0x28f7b, 0x26667),
            (0x28fe7, 0x26667),
            (0x29079, 0x26667),
            (0x2d1d4, 0x26667),
            (0x2d200, 0x26667),
            (0x2d230, 0x26667),
            (0x2d25e, 0x26667),
            (0x2d292, 0x26667),
            (0x2d2c3, 0x26667),
            (0x2d2f6, 0x26667),
            (0x2d327, 0x26667),
            (0x2d358, 0x26667),
            (0x2eb4d, 0x26667),
            (0x2eb6b, 0x26667),
            (0x2eb87, 0x26667),
            (0x2ec86, 0x26667),
            (0x2eca4, 0x26667),
            (0x2ecc0, 0x26667),
            (0x2edbf, 0x26667),
            (0x2eddd, 0x26667),
            (0x2edf5, 0x26667),
            (0x2ee2c, 0x26667),
            (0x2ee41, 0x26667),
            (0x2ee75, 0x26667),
            (0x2eea3, 0x26667),
            (0x28f60, 0x26667),
            (0x2663e, 0x26667),

            (0x26b41, 0x26941),  # Yes
            (0x283f8, 0x26941),

            (0x26b46, 0x26947),  # No
            (0x283fd, 0x26947),

            (0x26915, 0x26869),  # &5Not saved.

            (0x28953, 0x2894e),  # -
            (0x28958, 0x2894e),
            (0x2895d, 0x2894e),
            (0x28962, 0x2894e),
            (0x28967, 0x2894e),
            (0x28c7e, 0x2894e),
            (0x28c97, 0x2894e),

            (0x29033, 0x28caf),   # Attack
            (0x2903a, 0x28ca8),   # Recovery
            (0x29041, 0x28cc4),   # Special
            (0x2904a, 0x28cb6),   # Support
            (0x29051, 0x28cbd),   # Movement

            (0x28fea, 0x26ee1),   # &f
            (0x2907c, 0x26ee1),
            (0x2d1d7, 0x26ee1),
            (0x2d203, 0x26ee1),
            (0x2d233, 0x26ee1),
            (0x2d261, 0x26ee1),
            (0x2d295, 0x26ee1),
            (0x2d2a5, 0x26ee1),
            (0x2d2c6, 0x26ee1),
            (0x2d2d8, 0x26ee1),
            (0x2d2f9, 0x26ee1),
            (0x2d309, 0x26ee1),
            (0x2d32a, 0x26ee1),
            (0x2d33a, 0x26ee1),
            (0x2d35b, 0x26ee1),
            (0x2d36b, 0x26ee1),
            (0x2ee2f, 0x26ee1),
            (0x2ee44, 0x26ee1),
            (0x2ee78, 0x26ee1),
            (0x2eea6, 0x26ee1),
            (0x28f63, 0x26ee1),

            (0x2d0b8, 0x2d077),   # &c
            (0x2d132, 0x2d077),
            (0x2d173, 0x2d077),
            (0x2d2a2, 0x2d077),
            (0x2d2d5, 0x2d077),
            (0x2d306, 0x2d077),
            (0x2d337, 0x2d077),
            (0x2d368, 0x2d077),
            (0x2e9d3, 0x2d077),
            (0x2ea1c, 0x2d077),
            (0x2eb79, 0x2d077),
            (0x2ecb2, 0x2d077),

            (0x28f9f, 0x28c36), # Current Status
            (0x28faa, 0x28c41), # HP      /
            (0x28fb9, 0x28c50), # ZP      /
            (0x28fc8, 0x28c5f), # Status

            (0x271d2, 0x2718d), # &5You have nothing

            (0x26e68, 0x26e32), # Sell Items


    ],

    'ORBTL.EXE': [
            (0x28315, 0x282f8),
            (0x28332, 0x282f8),
            (0x2836e, 0x2834f),
            (0x2838d, 0x2834f),
            (0x283cb, 0x283ac),
            (0x28405, 0x283ea),
            (0x28420, 0x283ea),
            (0x2845a, 0x2843b),
            (0x28479, 0x2843b),
            (0x284b1, 0x28498),
            (0x284e7, 0x284ca),
            (0x28504, 0x284ca),
            (0x2853e, 0x28521),
            (0x28599, 0x28578),
            (0x285ba, 0x28578),
            (0x285f2, 0x285db),
            (0x28609, 0x285db),
            (0x2863f, 0x28620),
            (0x28683, 0x2865e),
            (0x286a8, 0x2865e),
            (0x286ee, 0x286cd),
            (0x2870f, 0x286cd),
            (0x2874d, 0x28730),

            (0x2d8d8, 0x2d5d2),
            (0x2d8e7, 0x2d5d2),
            (0x2d8f6, 0x2d5d2),
            (0x2d905, 0x2d5d2),
            (0x2d914, 0x2d5d2),
            (0x2d923, 0x2d5d2),

            (0x28c97, 0x27346),   # a:back1.gem
            (0x2738f, 0x27346),

            (0x2eab3, 0x2ea8e),  # Steal texts
            (0x2eac4, 0x2ea7a),
            (0x2eac9, 0x2ea7f),
            (0x2ead8, 0x2ea8e),
            (0x2eaec, 0x2eaa2),
            (0x2eafd, 0x2ea8e),
    ]
}
