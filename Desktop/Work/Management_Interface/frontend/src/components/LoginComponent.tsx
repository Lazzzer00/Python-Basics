import { Link } from "react-router-dom";
import SubmitButton from "./SubmitButton";
import CreateLoginWith from "./CreateLoginWith";

export default function LoginComponent() {
  return (
    <div className="bg-lightblack rounded-2xl p-[3rem] sm:w-full sm:h-full md:w-fit md:h-fit">
      <div className="pt-[3rem] lg:px-[10rem] md:px-[6rem] px-[5rem] pb-[2rem]">
        <h1 className="text-[3.2rem] text-textwhite text-center">Login</h1>
      </div>
      <form action="" method="" className="flex flex-col w-full">
        <label
          htmlFor="email"
          className="text-textwhite font-bold cursor-pointer"
        >
          Email
        </label>
        <input
          type="text"
          name="loginemail"
          id="email"
          autoComplete="off"
          placeholder="Type your email"
          className="bg-lightblack border-0 border-b-[1px] focus:outline-none focus:border-b-mainorange duration-200 py-2 px-[2px] mb-6 text-textwhite"
        />
        <label
          htmlFor="password"
          className="text-textwhite font-bold cursor-pointer"
        >
          Password
        </label>
        <input
          type="password"
          id="loginpassword"
          name="password"
          autoComplete="off"
          placeholder="Type your password"
          className="bg-lightblack border-0 border-b-[1px] focus:outline-none focus:border-b-mainorange duration-200 py-2 px-[2px] text-textwhite"
        />
        <div className="flex flex-row justify-between mt-[0.75rem]">
          <RememberMeButton />
          <Link
            to={"/passwordReset"}
            className="text-right text-mainorange focus:text-mainorange duration-500"
          >
            Forgot password?
          </Link>
        </div>
        <SubmitButton text={"LOGIN"} type={"submit"} />
        <SignUp />
      </form>
    </div>
  );
}

function SignUp() {
  return (
    <div className="flex flex-col mt-3 gap-[0.05em]">
      <p className="text-textwhite">
        Don't have an account?
        <Link to={"/createAccount"} className="text-mainorange">
          {" "}
          Sign Up
        </Link>
      </p>
      <CreateLoginWith />
    </div>
  );
}

function RememberMeButton() {
  return (
    <div className="flex gap-[0.3rem]">
      <input
        type="checkbox"
        id="rememberme"
        name="rememberme"
        className="accent-mainorange cursor-pointer"
      ></input>
      <label
        htmlFor="rememberme"
        className="text-textwhite hover:text-mainorange duration-500 cursor-pointer"
      >
        Remember me
      </label>
    </div>
  );
}
