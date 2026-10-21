# Run interface for Cog
# https://cog.run/python

from cog import BaseRunner, Input, Path


class Runner(BaseRunner):
    def setup(self) -> None:
        """Load the model into memory to make running multiple requests efficient"""
        # self.model = torch.load("./weights.pth")

    def run(
        self,
        image: Path = Input(description="Grayscale input image"),
        scale: float = Input(
            description="Factor to scale image by", ge=0, le=10, default=1.5
        ),
    ) -> Path:
        """Run the model on a single input"""
        return Path("rick.jpg")
