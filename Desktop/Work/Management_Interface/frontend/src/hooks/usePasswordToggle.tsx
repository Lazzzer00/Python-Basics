import React, { useState } from 'react'

export default function usePasswordToggle(defaultVisible: boolean | (() => boolean)): [boolean, React.Dispatch<React.SetStateAction<boolean>>, string] {
  const [visible, setVisible] = useState<boolean>(defaultVisible);
  const inputType = visible ? "text" : "password";

  return [visible, setVisible, inputType]
}
