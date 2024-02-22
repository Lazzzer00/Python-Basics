type CheckPasswordProps = {
  password1: string;
  password2: string;
};

export type PasswordState = "notLongEnough" | "passwordsNotEqual" | "noUpperCaseLetters" | "noLowerCaseLetters" | "noNumbers" | "validPasswords"; 

export type EmailState = "notLongEnough" | "no@Simbol" | "containsUppercaseLetters" | "validEmail";

export type FormSubmitProps = {
  email: string;
  username: string
} & CheckPasswordProps;

export function checkPassword({ password1, password2 }: CheckPasswordProps): PasswordState {
  const numberCheck: RegExp = /[0-9]/;
  const upperCheck: RegExp = /[A-Z]/;
  const lowerCheck: RegExp = /[a-z]/;

  if (password1.length < 8) {
    return "notLongEnough"
  }
  if (password1 !== password2) {
    return "passwordsNotEqual";
  }
  if (!numberCheck.test(password1)) {
    return "noNumbers";
  }
  if (!lowerCheck.test(password1)) {
    return "noLowerCaseLetters"
  }
  if (!upperCheck.test(password1)) {
    return "noUpperCaseLetters";
  }
  return "validPasswords";
} 

export function checkEmail(email: string): EmailState {
  const upperCheck: RegExp = /[A-Z]/;
  const AtSymbolCheck: RegExp = /[@]/;
  if (AtSymbolCheck.test(email)) {
    return "no@Simbol";
  }
  if (email.length < 6) {
    return "notLongEnough"
  }
  if (upperCheck.test(email)) {
    return "containsUppercaseLetters";
  }
  return "validEmail";
}
