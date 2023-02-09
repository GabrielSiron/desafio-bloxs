import { Header, Page, MenuItem, Text,
    Logo, AmountCard, Line, TitleCard, TransactionsContainer,
    AmountValue, DepositButton, DraftButton, TransactionsList } from './style';

import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';

import { UserContext } from '../../contexts/user';
import { useState, useContext, useEffect } from 'react';
import { Get, GetFirstPage } from '../../services/crud';
import Transaction from '../../components/Transaction/index';

const Home = () => {
    const { email, password, name, cpf, setToken, setEmail, setPassword } = useContext(UserContext);

    const [loading, setLoading] = useState(false);
    const [account, setAccount] = useState({message: '', amount: 0, name: ''});
    const [transactions, setTransactions] = useState([])
    

    useEffect(() => {
        const GetAccountInfo = async () => {
            let token = sessionStorage.getItem('token') || '';
            await Get('account', token, setAccount);
            
        }

        const GetTransactions = async () => {
            let token = sessionStorage.getItem('token') || '';
            GetFirstPage('transactions', '1', token, setTransactions)
        }

        GetTransactions()
        GetAccountInfo()
        
    }, [])

    return(
        <Page>
            <Header>
                <Logo src={LogoTotal}/>
                <MenuItem>
                    <Text>Sobre</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Transações</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Menu</Text>
                </MenuItem>
            </Header>
            <Line>
                <AmountCard>
                    <TitleCard>Saldo</TitleCard>
                    <AmountValue>{ 'R$ ' + account.amount }</AmountValue>
                </AmountCard>
                <DepositButton type='button'>Depositar</DepositButton>
                <DraftButton type='button'>Sacar</DraftButton>
            </Line>
            <Line>
                <TransactionsContainer>
                    <TitleCard>Transações</TitleCard>
                    <TransactionsList>
                        {
                            transactions.map((obj, i) => <Transaction></Transaction>)
                        }
                    </TransactionsList>
                </TransactionsContainer>
            </Line>
        </Page>
    )
}

export default Home;