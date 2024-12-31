        AREA question1, CODE, READONLY
        ENTRY
        LDR   r0, =UPC                ; initialize r0 to beginning of upc
        MOV   r1, #0                  ; initialize index
        MOV   r2, #0                  ; initialize r2 with 0 to act as the even sum
        MOV   r3, #0                  ; initialize r3 with 0 to act as the odd sum
Loop1   LDRB  r4, [r0, r1]            ; loading current character into individual registers
        TST   r4, #1                  ; check if least significant binary bit is 1 because the binary number would be +2^0=+1
        BEQ   isEven                  ; if TST returns 0, the code will continue at isEven
        ADD   r3, r3, r4              ; otherwise the odd sum will be updated
isEven  ADD   r2, r2, r4              ; if TST returns 1, the even sum will be updated
        ADD   r1, r1, #1              ; increment index
        CMP   r1, #11                 ; check if index is at end of string
        BNE   Loop1                   ; loops until entire string has been added
Check   EQU   r4
Mult    EQU   3                       ; initialize Multiplication constant Mult to 3
        MLA   r5, r2, #Mult, r3       ; step 3
        ADD   r6, #Check, r5          ; sums check and total from first three steps
Repeat  SUB   r6, r6, #10             ; repeatedly subtract ten until 0 is reached
        TSTGE r6, #0                  ; check if result is greater than or equal to 0
        BEQ   Repeat                  
        TST   r6, #0                  ; check if result is equal to 0
        BEQ   Valid
        STR   #2, r0                  ; stores 2 if invalid
Valid   STR   #1, r0                  ; stores 1 if valid
Loop2   B Loop2

        AREA question1, DATA, READWRITE
UPC     DCB "013800150738"
        END