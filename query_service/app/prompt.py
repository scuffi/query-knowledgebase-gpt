class Prompt:
    def __init__(self, *args, **kwargs) -> None:
        """
        Any variables passed in positionally will plaintext in the prompt, any arguments
        passed in through keywords will be added to the prompt as a seperate section,
        where the argument name is the section name, so name your variables carefully!
        """
        self.positional = args
        self.kw = kwargs
    
    def build(self):
        """
        This function generates a prompt string based on the positional and keyword arguments of an object.
        
        Returns:
          The `build` method is returning a string prompt that includes the positional arguments and keyword
        arguments of the object, followed by a specific Response clause.
        """
        prompt = f"""
{', '.join(self.positional)}
{self._generate_kw()}
### Response:
        """
        
        return prompt
        
    def _generate_kw(self):
        """
        This function generates a string containing formatted key-value pairs from a dictionary.
        
        Returns:
          The `_generate_kw` method is returning a string that contains formatted key-value pairs from the
        `kw` dictionary attribute of the object. Each key-value pair is formatted as a string with the key
        title-cased and the value enclosed in single quotes. The string is created by joining these
        formatted strings with newline characters.
        """
        return '\n'.join([f"### {key.replace('_', ' ').title()}: '{value}'" for key, value in self.kw.items()])
    
    # Allow for str and repr interpretations of the prompt to be the built prompt.
    __repr__ = build
    __str__ = build