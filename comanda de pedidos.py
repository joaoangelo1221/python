pedido = {}
while True:
  num = int(input("Número do pedido: "))
  cliente = input("Cliente: ")
  end = input("Endereço: ")
  cont = int(input("Contato: "))
  pedido.update({num: [cliente, end, cont]})
  resp = input("Deseja continuar [S|N]? ")
  print(f"Pedido: {pedido}")
  if resp == "n" or resp == "N":
    print("\n")
    break
resp = input("Deseja alterar o pedido [S|N]? ")
if resp == "n" or resp == "N":
  print("\n")
else: 
  pedido0 = int(input("Qual pedido você deseja alterar?: "))
  cliente = input("Cliente: ")
  end = input("Endereço: ")
  cont = int(input("Contato: "))
  if pedido0 in pedido:
    pedido.update({num: [cliente, end, cont]})
    print("Pedido alterado com sucesso")
    for num_pedido0, alteracao in pedido.items():
      print(f"Pedido: {num_pedido0}")
      print(f"Cliente: {alteracao [0]}")
      print(f"Endereço: {alteracao [1]}")
      print(f"Contato: {alteracao [2]}")
  else:
    print("inválido")