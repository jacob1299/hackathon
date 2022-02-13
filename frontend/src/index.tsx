import { ColorModeScript } from "@chakra-ui/react"
import * as React from "react"
import ReactDOM from "react-dom"
import { App } from "./App"
import reportWebVitals from "./reportWebVitals"
import * as serviceWorker from "./serviceWorker"
import { ChakraProvider } from '@chakra-ui/react'
import { Auth0Provider } from '@auth0/auth0-react'
import { BrowserRouter } from 'react-router-dom'



ReactDOM.render(
  <BrowserRouter>
    <Auth0Provider domain='dev-nrag6ly2.us.auth0.com' clientId='tIxzBNENWmQotMM4yAL7gHBDUUKXtX89' redirectUri={window.location.origin}>
      <ChakraProvider >
      <React.StrictMode>
        <ColorModeScript />
        <App />
      </React.StrictMode>
    </ChakraProvider >
    </Auth0Provider>
  </BrowserRouter>
  ,
  document.getElementById("root"),
)

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
serviceWorker.unregister()

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
