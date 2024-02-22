import "./styles/index.css";
import { Routes, Route, Link } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import PasswordReset from "./pages/PasswordResetPage";
import CreateAccountPage from "./pages/CreateAccountPage";

export default function App() {
  return (
    <div className="h-full">
      <Routes>
        <Route path="" element={<Link to={"/login"}>Go to login</Link>} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/passwordReset" element={<PasswordReset />} />
        <Route path="/createAccount" element={<CreateAccountPage />}>
          <Route path="/createAccount/google" />
          <Route path="/createAccount/github" />
          <Route path="/createAccount/facebook" />
        </Route>
      </Routes>
    </div>
  );
}
