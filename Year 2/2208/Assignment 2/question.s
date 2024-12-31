          AREA question, CODE, READWRITE
          ENTRY
          ADR r0, STRING1
          ADR r1, STRING2
          MOV r2, #0               ; check counter

Load      LDRB r3, [r0], #1        ; load first byte of string, updates pointer so register counter not needed
          ADD r2, r2, #1           ; iteration counter
          CMP r3, #0x00            ; first check if it is the end of the line
          STRBEQ r3, [r1, #1]!     ;
          BEQ Loop                 ; skips to the end of the program because the string has ended

          CMP r3, #0x74            ; checks for t
          STRBNE r3, [r1, #1]!     ; stores if no match
          BNE Load
          LDRBEQ r4, [r0], #1      ; loads next character to check for h

          CMPEQ r4, #0x68          ; checks for h
          STRBNE r3, [r1, #1]!     ; stores first character
          STRBNE r4, [r1, #1]!     ; so second character is also stored when not a match
          BNE Load
          LDRBEQ r5, [r0], #1      ; loads next character to check for e

          CMPEQ r5, #0x65          
          STRBNE r3, [r1, #1]!     ; stores first space if not a match
          STRBNE r4, [r1, #1]!     ; stores first character if not a match
          STRBNE r5, [r1, #1]!     ; stores second character if not a match
          BNE Load
          LDRBEQ r6, [r0], #1      ; loads next character to check for space or null

          CMPEQ r6, #0x20          
          CMPNE r6, #0x00
          STRBNE r3, [r1, #1]!     ; stores first space if not a match
          STRBNE r4, [r1, #1]!     ; stores first character if not a match
          STRBNE r5, [r1, #1]!     ; stores second character if not a match
          STRBNE r6, [r1, #1]!     ; stores third character if not a match
          B Load                   ; skips storing and gets the next character if it matches
Loop      B     Loop

          AREA question, DATA, READWRITE
STRING1   DCB   "4the the 4the The the the1"
EoS       DCB   0x00
STRING2   SPACE 0x7F
          END