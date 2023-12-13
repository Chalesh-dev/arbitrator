import '@openzeppelin/contracts/token/ERC20/ERC20.sol';
import '@uniswap/v3-core/contracts/libraries/FixedPoint96.sol';
import '@uniswap/v3-core/contracts/libraries/FullMath.sol';
import '@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol';
import '@uniswap/v3-core/contracts/interfaces/IUniswapV3Factory.sol';

function calculatePriceFromLiquidity(
  address token0,
  address token1,
  uint24 fee,
  address factory
) public view returns (uint256) {
  IUniswapV3Pool pool = IUniswapV3Pool(IUniswapV3Factory(factory).getPool(token0, token1, fee));
  (uint160 sqrtPriceX96, , , , , , ) = pool.slot0();

  uint256 amount0 = FullMath.mulDiv(pool.liquidity(), FixedPoint96.Q96, sqrtPriceX96);

  uint256 amount1 = FullMath.mulDiv(pool.liquidity(), sqrtPriceX96, FixedPoint96.Q96);

  return (amount1 * 10**ERC20(token0).decimals()) / amount0;
}