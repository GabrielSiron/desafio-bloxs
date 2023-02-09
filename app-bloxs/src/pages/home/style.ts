import styled from "styled-components";

export const Header = styled.div `
    position: relative;
    width: 95vw;
    height: 60px;
    float: left;
`

export const MenuItem = styled.button `
    width: 120px;
    height: 60px;
    background-color: #fff;
    border: none;
    float: right;
    margin-right: 20px;
    text-align: center;
`

export const Text = styled.span `
    font-family: 'poppins';
    font-size: 1.0rem;
`

export const Page = styled.div `
    width: 100vw;
    height: 100vh;
    background-color: #fff;
`

export const Logo = styled.img `
    width: 120px;
    height: auto;
    float: left;
    padding: 20px;
    padding-left: 40px;
`

export const Line = styled.div `
    padding-top: 60px;
    width: 100vw;
    display: flex;
    justify-content: center !important;
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

export const DepositButton = styled.button `
    width: 100px;
    height: 120px;
    font-family: 'poppins-medium';
    font-size: 1.0rem;
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

export const DraftButton = styled.button `
    width: 100px;
    height: 120px;
    font-family: 'poppins-medium';
    font-size: 1.0rem;
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
`

export const TransactionsList = styled.div `
    width: 100%;
    height: 200px;
    overflow-y: scroll;

`