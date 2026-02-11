if OBJECT_ID('vwFatoVendas', 'V') is not null
    drop view vwFatoVendas

exec('
    create view vwFatoVendas as
    select
        pedidos.idPedido,
        pedidos.dataPedido,
        clientes.nomeCliente,
        vendedores.nomeVendedor,
        regionais.nomeRegional,
        produtos.nomeProduto,
        linhasProdutos.nomeLinhaProduto,
        itensPedido.quantidade,
        itensPedido.precoUnitario,
        itensPedido.desconto,
        itensPedido.quantidade * (
            itensPedido.precoUnitario - itensPedido.desconto)
            ) as valor_total

        from pedidos 
        join clientes on pedidos.fkCliente = clientes.idPedido
        join vendedores on pedidos.fkVendedor = vendedores.idVendedor 
        join regionais on vendedores.fkRegional = regionais.idRegional
        join itensPedidos on itensPedido.fkPedido = pedidos.IdPedido
        join produtos on itensPedido.fkProduto = produtos.idProduto
        join linhasProduos on produtos.fkLinhaProduto = linhasProdutos.idLinhaProduto
')