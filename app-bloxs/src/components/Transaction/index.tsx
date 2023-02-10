import { useEffect, useState } from 'react';
import { Element, Title, Value, DateElement } from './style';

const Transaction = (props: any) => {
    
    const [date, setDate] = useState('')

    useEffect(() => {
        const formatDate = () => {
            console.log(typeof props.transaction.date);
            
            let datetime = new Date(props.transaction.date).toISOString();
            let partial_date = datetime.split('T');
            let date_splited = partial_date[0].split('-');
            let aux = date_splited[2];
            date_splited[2] = date_splited[0];
            date_splited[0] = aux;
            setDate(date_splited.join('/'));
            
            
        }
    
        formatDate();

    }, [])
    return(
        <Element>
            <Title>{props.transaction.is_sender? 'Transferência Enviada' : 'Transferência Recebida'}</Title>
            <DateElement>{date}</DateElement>
            <Value>{'R$ ' + props.transaction.value}</Value>
        </Element>
    )
}

export default Transaction;