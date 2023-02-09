import { Element, Title, Value } from './style';

const Transaction = (props: any) => {
    
    return(
        <Element>
            <Title>{props.transaction.is_sender? 'Transferência Enviada' : 'Transferência Recebida'}</Title>
            <Value>{props.transaction.value}</Value>
        </Element>
    )
}

export default Transaction;