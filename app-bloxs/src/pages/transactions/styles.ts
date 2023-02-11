import styled from "styled-components";

export const TransactionsCard = styled.div `
    width: 700px;
    margin: 10px calc(50% - 350px);
    height: 400px;
    background-color: #f2f2f2;
    border-radius: 12px;
`

export const TransactionsContainer = styled.div `
    width: 90%;
    margin: 5%;
    height: 320px;
    overflow-y: scroll;
    background-color: #fff;
    border-radius: 12px;
`



export const Line = styled.div `
    padding-top: 20px;
    width: 100vw;
    display: flex;
    justify-content: center !important;
`

export const SeeMore = styled.button `
    width: 90%;
    height: 40px;
    border: none;
    border-radius: 12px;
    margin: 6px 5%;
    padding: 0px;
    font-family: 'poppins-medium';
    color: #fff;
    background-color: #AAD0FF;
    background-color: ${props=>props.disabled ? '#AAD0FF' : '#57A0FF'};
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    border: none;
    border-radius: 12px;
    transition: .2s ease-out;
    &:hover{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#80b7ff'};
    }
    &:active{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#377ad2'};
    }
`