import styled from "styled-components";

export const Header = styled.div `
    position: relative;
    width: 95vw;
    height: 60px;
    float: left;
`

export const MenuItem = styled.button `
    @keyframes changeText {
        from {font-size: 1.0rem;}
        to {font-size: 1.2rem;}
    }
    width: 120px;
    height: 60px;
    background-color: #fff;
    border: none;
    float: right;
    font-size: 1.0rem;
    margin-right: 20px;
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    text-align: center;
`

export const Logo = styled.img `
    width: 120px;
    height: auto;
    float: left;
    padding: 20px;
    padding-left: 40px;
`



export const AmountCard = styled.div `
    width: 300px;
    height: 120px;
    background-color: #f2f2f2;
    border-radius: 12px;
`

export const TitleCard = styled.h2 `
    padding: 30px;
    padding-bottom: 10px;
    font-family: 'poppins-medium';
    font-size: 1.0rem;
`

export const AmountValue = styled.span `
    padding: 30px;
    font-family: 'poppins';
    font-size: 1.8rem;
`

export const ActionButton = styled.button `
    width: 100px;
    height: 120px;
    font-family: 'poppins-medium';
    color: #fff;
    background-color: ${props=>props.disabled ? '#AAD0FF' : '#57A0FF'};
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    border: none;
    border-radius: 12px;
    transition: .2s ease-out;
    margin-left: 20px;
    &:hover{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#80b7ff'};
    }
    &:active{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#377ad2'};
    }
`

export const TransactionsContainer = styled.div `
    width: 540px;
    height: 300px;
    background-color: #f2f2f2;
    border-radius: 12px;
    box-sizing: border-box;
    padding-bottom: 20px;
`

export const TransactionsList = styled.div `
    width: 100%;
    height: 200px;
    overflow-y: scroll;

`

export const TransactionCard = styled.div `
    width: 540px;
    height: 60px;
    background-color: #f2f2f2;
    border-radius: 12px;
`

export const InputValue = styled.input`
    margin: 10px;
    padding: 10px;
    font-size: 1.0rem;
    height: 40px;
    box-sizing: border-box;
    border-radius: 8px;
    font-family: 'inter-regular'; 
    outline: 0;
`

export const MoneyPlaceholder = styled.span `
    font-family: 'poppins-bold';
    font-size: 1.0rem;
    margin: 10px;
    margin-right: 0px;
`

export const SendButton = styled.button `
    width: 140px;
    height: 40px;
    font-family: 'poppins-medium';
    font-size: 1.0rem;
    color: #fff;
    background-color: ${props=>props.disabled ? '#AAD0FF' : '#57A0FF'};
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    border: none;
    border-radius: 12px;
    transition: .2s ease-out;
    margin: 10px;
    float: right;
    &:hover{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#80b7ff'};
    }
    &:active{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#377ad2'};
    }
`
