import { TransactionCard, InputValue,
    AmountCard, TitleCard, TransactionsContainer, MoneyPlaceholder,
    AmountValue, ActionButton, SendButton, TransactionsList } from './style';

import { Header, Line, MenuItem, Page, Logo } from '../../styles/common-structure';

import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';

import { UserContext } from '../../contexts/user';
import { useState, useContext, useEffect } from 'react';
import { Get, GetFirstPage, Create } from '../../services/crud';
import Transaction from '../../components/Transaction/index';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const { setToken } = useContext(UserContext);

    const [loading, setLoading] = useState(false);
    const [account, setAccount] = useState({message: '', amount: 0, name: ''});
    const [transactions, setTransactions] = useState([])
    const [deposit, setDeposit] = useState(false)
    const [withdraw, setWithdraw] = useState(false)
    const [value, setValue] = useState('')

    let navigate = useNavigate();

    const Logout = () => {
        sessionStorage.removeItem('token');   
        setToken('')
        navigate('/signin')
    }

    const RefreshValue = (event: React.ChangeEvent<HTMLInputElement>)=>{
        setValue(event.target.value)
    }

    const changeDepositValue = () => {
        setValue('0')
        setDeposit(!deposit)
        setWithdraw(false)
    }

    const changeWithdrawnValue = () => {
        setValue('0')
        setWithdraw(!withdraw)
        setDeposit(false)
    }
    
    const CreateDeposit = () => {
        let token = sessionStorage.getItem('token') || '';
        let date = new Date();
        let user_id = sessionStorage.getItem('user_id');
        let body = {
            'value': value,
            'transaction_date': date.toISOString().slice(0, 19),
            'transfer_receiver_id': user_id,
            'transfer_sender_id': null
        }

        Create('transaction', token, body, [GetTransactions, GetAccountInfo])
        
        
    }

    const CreateWithdraw = () => {
        let token = sessionStorage.getItem('token') || '';
        let date = new Date();
        let user_id = sessionStorage.getItem('user_id');
        let body = {
            'value': value,
            'transaction_date': date.toISOString().slice(0, 19),
            'transfer_receiver_id': null,
            'transfer_sender_id': user_id
        }

        Create('transaction', token, body, [GetTransactions, GetAccountInfo])
    }

    const GetAccountInfo = async () => {
        let token = sessionStorage.getItem('token') || '';
        await Get('account', token, setAccount);
        
    }

    const goToTransactions = () => {
        navigate('/transactions')
    }

    const GetTransactions = async () => {
        let token = sessionStorage.getItem('token') || '';
        GetFirstPage('transactions', '1', token, setTransactions)
    }

    useEffect(() => {

        let token = sessionStorage.getItem('token') || ''
        
        if(token.length == 0){
            navigate('/signin')
        }

        GetTransactions()
        GetAccountInfo()
        
    }, [])

    return(
        <Page>
            <Header>
                <Logo src={LogoTotal}/>
                <MenuItem onClick={Logout}>
                    Sair
                </MenuItem>
                <MenuItem>
                    Sobre
                </MenuItem>
                <MenuItem onClick={goToTransactions}>
                    Transações
                </MenuItem>
            </Header>
            <Line>
                <AmountCard>
                    <TitleCard>Saldo</TitleCard>
                    <AmountValue>{ 'R$ ' + account.amount }</AmountValue>
                </AmountCard>
                <ActionButton type='button' onClick={changeDepositValue}>Depositar</ActionButton>
                <ActionButton type='button' onClick={changeWithdrawnValue}>Sacar</ActionButton>
            </Line>
            {
                deposit?
                <Line>
                    <TransactionCard>
                        <MoneyPlaceholder>R$</MoneyPlaceholder>
                        <InputValue onChange={RefreshValue}></InputValue>
                        <SendButton onClick={CreateDeposit}>Depositar</SendButton>
                    </TransactionCard>
                </Line>
                :
                <></>
            }
            {
                withdraw?
                <Line>
                    <TransactionCard>
                        <MoneyPlaceholder>R$</MoneyPlaceholder>
                        <InputValue onChange={RefreshValue}></InputValue>
                        <SendButton onClick={CreateWithdraw}>Sacar</SendButton>
                    </TransactionCard>
                </Line>
                :
                <></>
            }
            <Line>
                <TransactionsContainer>
                    <TitleCard>Últimas Transações</TitleCard>
                    <TransactionsList>
                        {
                            transactions.map((transaction, i) => <Transaction transaction={transaction}></Transaction>)
                        }
                    </TransactionsList>
                </TransactionsContainer>
            </Line>
        </Page>
    )
}

export default Home;