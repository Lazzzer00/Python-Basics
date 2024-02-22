import usePasswordToggle from "../hooks/usePasswordToggle";
import EyePasswordShow from "../assets/eye-password-show.svg";
import EyePasswordHide from "../assets/eye-password-hide.svg";
import SubmitButton from "./SubmitButton";
import CreateLoginWith from "./CreateLoginWith";
import { ChangeEvent, useRef, useState } from "react";
import { NavigateFunction, useNavigate } from "react-router-dom";

const navigate: NavigateFunction = useNavigate();

type WarningType = "warning" | "safe";

export default function CreateAccountComponent() {
  const [visible1, setVisible1, inputType1] = usePasswordToggle(false);
  const [visible2, setVisible2, inputType2] = usePasswordToggle(false);
  const [warning, setWarning] = useState<WarningType>("safe");
  const emailInputRef = useRef<HTMLInputElement>(null);
  const usernameInputRef = useRef<HTMLInputElement | null>(null);
  const passwordInputRef1 = useRef<HTMLInputElement | null>(null);
  const passwordInputRef2 = useRef<HTMLInputElement | null>(null);

  return (
    <div className="bg-lightblack rounded-2xl p-[3rem] sm:w-full sm:h-full md:w-fit md:h-fit">
      <div className="pt-[3rem] lg:px-[10rem] md:px-[6rem] px-[5rem] pb-[2rem]">
        <h1 className="text-[3.2rem] text-textwhite text-center">Sign Up</h1>
      </div>
      <form
        action="/createUser"
        method="post"
        className="flex flex-col w-full"
        onSubmit={(): void => {
          const email = emailInputRef.current?.value;
          const username = usernameInputRef.current?.value;
          const password1 = passwordInputRef1.current?.value;
          const password2 = passwordInputRef2.current?.value;
          if (!email || !username || !password1 || !password2) {
            setWarning("warning");
          } else {
            navigate("/home");
          }
        }}
      >
        <label
          htmlFor="email"
          className="text-textwhite font-bold cursor-pointer"
        >
          Email
        </label>
        <input
          ref={emailInputRef}
          onChange={(event: ChangeEvent<HTMLInputElement>) => {
            if (emailInputRef.current) {
              emailInputRef.current.value = event.target.value;
            }
          }}
          type="email"
          name="signupemail"
          id="email"
          autoComplete="off"
          placeholder="Type your email"
          className="bg-lightblack border-0 border-b-[1px] focus:outline-none focus:border-b-mainorange duration-200 py-2 px-[2px] mb-6 text-textwhite"
        />
        <label
          htmlFor="username"
          className="text-textwhite font-bold cursor-pointer"
        >
          Username
        </label>
        <input
          ref={usernameInputRef}
          onChange={(event: ChangeEvent<HTMLInputElement>) => {
            if (usernameInputRef.current) {
              usernameInputRef.current.value = event.target.value;
            }
          }}
          type="text"
          name="signupusername"
          id="username"
          autoComplete="off"
          placeholder="Type your email"
          className="bg-lightblack border-0 border-b-[1px] focus:outline-none focus:border-b-mainorange duration-200 py-2 px-[2px] mb-6 text-textwhite"
        />
        <label
          htmlFor="password1"
          className="text-textwhite font-bold cursor-pointer"
        >
          Create a password
        </label>
        <div className="flex justify-between">
          <input
            ref={passwordInputRef1}
            onChange={(event: ChangeEvent<HTMLInputElement>) => {
              if (passwordInputRef1.current) {
                passwordInputRef1.current.value = event.target.value;
              }
            }}
            type={inputType1}
            id="password1"
            name="signuppassword"
            autoComplete="off"
            placeholder="(8 + characters, must include capital letters and numbers)"
            className="bg-lightblack border-0 border-b-[1px] focus:outline-none focus:border-b-mainorange duration-200 py-2 px-[2px] text-textwhite mb-6 w-full"
          />
          <button onClick={() => setVisible1((prev) => !prev)} type="button">
            {visible1 ? (
              <img
                src={EyePasswordShow}
                alt="Password Show / Hide"
                className="h-[30px] m-2"
              />
            ) : (
              <img
                src={EyePasswordHide}
                alt="Password Show / Hide"
                className="h-[30px] m-2"
              />
            )}
          </button>
        </div>
        <label
          htmlFor="password2"
          className="text-textwhite font-bold cursor-pointer"
        >
          Confirm Password
        </label>
        <div className="flex justify-between">
          <input
            ref={passwordInputRef2}
            onChange={(event: ChangeEvent<HTMLInputElement>) => {
              if (passwordInputRef2.current) {
                passwordInputRef2.current.value = event.target.value;
              }
            }}
            type={inputType2}
            id="password2"
            autoComplete="off"
            placeholder="Type your password"
            className="bg-lightblack border-0 border-b-[1px] focus:outline-none focus:border-b-mainorange duration-200 py-2 px-[2px] text-textwhite w-full"
          />
          <button onClick={() => setVisible2((prev) => !prev)} type="button">
            {visible2 ? (
              <img
                src={EyePasswordShow}
                alt="Password Show / Hide"
                className="h-[30px] m-2"
              />
            ) : (
              <img
                src={EyePasswordHide}
                alt="Password Show / Hide"
                className="h-[30px] m-2"
              />
            )}
          </button>
        </div>
        <p className="text-textwhite">Not valid info</p>
        <SubmitButton text={"CREATE ACCOUNTaa"} type={"submit"} />
      </form>
      <div className="flex flex-col mt-3 gap-[0.05em]">
        <p className="text-textwhite">Or create an account with</p>
        <CreateLoginWith />
      </div>
    </div>
  );
}
