import { Link } from "react-router-dom";

type SubmitButtonProps = {
  type: "submit" | "reset" | "button" | undefined;
  text: string;
};

export default function LoginButton(props: SubmitButtonProps) {
  return (
    <Link to={"/"} className="text-textwhite text-center mt-[2em] ">
      <button
        type={props.type}
        className="w-full border-[1px] border-mainorange rounded-3xl py-2 hover:bg-mainorange duration-[750ms] hover:text-darkblack hover:font-bold hover:border-lightblack"
      >
        {props.text}
      </button>
    </Link>
  );
}
