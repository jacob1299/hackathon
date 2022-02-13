import * as React from "react"
import {
  ChakraProvider,
  Box,
  Text,
  Link,
  VStack,
  Code,
  Grid,
  theme,
  Center, 
  Flex
} from "@chakra-ui/react"
import { LoginButton } from './components/LoginButton'
import { Nav } from './components/Nav'
import { Routes, Route } from 'react-router-dom'
import { MainPage } from './pages/MainPage'


export const App = () => (
    <ChakraProvider theme={theme}>
      <Nav />
      <Flex h='100vh' w='100vw'>
        <Center bg='green.400' h='100%' color='white' w='full'>
          <Routes>
            <Route path="/" element={<LoginButton />} />
            <Route path="/main" element={<MainPage />} />
          </Routes>
        </Center>
      </Flex>
    </ChakraProvider>  
)
