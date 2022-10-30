#14 done perfectly
#Remove indentation - indentation - AST chara - strip() diye len before and after

#code with atoms
previous_value = 1

a = 1
b = 10
#infix_operator_precedence
value = a - b / 2
value = a + 2 * b

#post_inc_dec
value = previous_value++
value_new = previous_value_new++

#pre_inc_dec
value = ++previous_value

var2 = 22

#constant_variable 
new_value = value
var1=var2
var3="saaj"

value = 33
v = 35
v1 = 8

#conditional_operator
new_value = value == 3 ? 2 : 1
v1 == 3? 2 : 1 + v == 5
if v1==3 {v2=2} else {v2=1}

#arithmetic_as_logic
(new_value-3)*(value-4)!=0
v1!=3 && v2!=4

#logic_as_control_flow 
new_value == ++new_value > 0 || ++value > 0
v2 == --v1 < 9 && v2++ = 0;

#repurposed_variable
for (int i = 0; i<22; i++)
for (int j = 0; j<8; i++)
        print("repurposed variable")
        
for (int v1 = 0; v1<99; v1++)
    for (int v2 = 0; v2<6; v2++)
        print("repurposed variable")

for (int v1 = 0; ...; v1++)
for (int v2 = 0; ...; v1++)

#dead_repeated
v1 = 1 
v1 = 2
v2 = 4 
v2 = v2 + 1 

#omitted_curly_braces
if (v1) f1(); f2();
if (v1) {f1()}; f2();

#type_conversion
v1 = (int) 1.99f;
v1 = (int) Math.ceil(1.99f);
v1 = (int) Math.floor(1.99f);

#cole
v1 = 013
le = 0768
oc = 0523656

#remove indentation atom
while (v2 > 0):
        v2 = v2 - 1
        v1 = v1 - 1

while (v2 > 0):
        v3 = v3 - 1
v4 = v2 - 1

#indentation atom
while (v2 > 0): {v3 = v2 - 1}
        v2 = v4 - 1

while (v2 > 0): {v1 = v2 - 1}
v1 = v3 - 1

if (v1>3) {}
        v2 = "Saaj"

if (v1<5) {}
v3 = "Saaj"

for (int v1 = 0; ...; v1++) {}
j = "pop"


